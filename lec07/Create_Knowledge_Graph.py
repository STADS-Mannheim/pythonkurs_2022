import pandas as pd
import os
import numpy as np
from collections import Counter

input_directory = "/Users/lucaslinden/Pythonkurs/GKG_Daten"
files = os.listdir(input_directory)
person = 'joe biden'

def kleinschreibung(x):
    # Kleinschreibung
    x = {k.lower() : x[k] for k in x.keys()}
    return x

def find_person(x, person):
    # Finde Organisation
    return x.get(person, -1)

def compute_distances(x, person, type):
    organization_position = x[person]
    persons_dict = {term: np.absolute(x[type][term] - organization_position) for term in x[type].keys() if
                    term != person}
    return persons_dict

def get_rank(df,column,asc):
    df_temp = df.sort_values(by=column,ascending=asc)
    return {df_temp.index[i-1]: i for i in range(1,len(df.index)+1)}

for file in files:
    try:
        file_path = input_directory + '/' + file
        df = pd.read_parquet(file_path)
    except:
        df = pd.DataFrame()

    if len(df)>0:
        # Kleinschreibung
        df.PERSONS = df.PERSONS.apply(lambda x: kleinschreibung(x))
        df.ORGANIZATIONS = df.ORGANIZATIONS.apply(lambda x: kleinschreibung(x))

        # Finde alle Artikel, die die Organization enthalten und lösche alle anderen
        df[person] = df.PERSONS.apply(lambda x: find_person(x, person))
        df = df[df[person] != -1]

        # Berechne Abstände im Text
        df.PERSONS = df.apply(lambda x: compute_distances(x, person, 'PERSONS'), axis=1)
        df.ORGANIZATIONS = df.apply(lambda x: compute_distances(x, person, 'ORGANIZATIONS'), axis=1)

        # Berechne Anzahl der Nennungen
        persons = [key.lower() for sublist in df.PERSONS.values.tolist() for key in sublist.keys() if key.lower() != person]
        organizations = [key.lower() for sublist in df.ORGANIZATIONS.values.tolist() for key in sublist.keys()]

        ##### Plausibility Check ######
        print(Counter(persons).most_common(10))
        print(Counter(organizations).most_common(10))
        person_mentions = dict(Counter(persons))
        organization_mentions = dict(Counter(organizations))

        # Berechne durchschnittliche Entfernung
        persons_mean = {k: np.mean([d.get(k) for d in df.PERSONS.values.tolist() if d.get(k) != None]) for k in persons}
        organization_mean = {k: np.mean([d.get(k) for d in df.ORGANIZATIONS.values.tolist() if d.get(k) != None]) for k in organizations}

        ##### Plausibility Check ####
        print(sorted(persons_mean, key=persons_mean.get, reverse=False)[:10])
        print(sorted(organization_mean, key=organization_mean.get, reverse=False)[:10])

        # combine dicts
        person_dict = {person: {'mentions': person_mentions.get(person), 'mean': persons_mean.get(person)} for person in persons}
        person_df = pd.DataFrame.from_dict(person_dict,orient='index')
        ranked_dicts = [get_rank(person_df,'mentions',False),get_rank(person_df,'mean',True)]
        comb_dict = {person: (ranked_dicts[0].get(person) + ranked_dicts[1].get(person))/2 for person in person_df.index}
        final_persons_df = pd.DataFrame.from_dict(comb_dict,orient='index').rename(columns={0:'Ranking'}).sort_values(by='Ranking')

        organization_dict = {organization: {'mentions': organization_mentions.get(organization), 'mean': organization_mean.get(organization)} for organization in organizations}
        organization_df = pd.DataFrame.from_dict(organization_dict,orient='index')
        ranked_dicts = [get_rank(organization_df, 'mentions', False), get_rank(organization_df, 'mean', True)]
        comb_dict = {organization: (ranked_dicts[0].get(organization) + ranked_dicts[1].get(organization)) / 2 for organization in organization_df.index}
        final_organization_df = pd.DataFrame.from_dict(comb_dict, orient='index').rename(columns={0: 'Ranking'}).sort_values(
            by='Ranking')

        print(final_persons_df.head(10))
        print(final_organization_df.head(10))


