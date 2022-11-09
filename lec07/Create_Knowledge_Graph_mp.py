import pandas as pd
import os
import numpy as np
from collections import Counter
import multiprocessing as mp

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

def create_ranking_file(params):
    input_directory = params['input_directory']
    file = params['file']
    person = params['person']
    output_directory = params['output_directory']

    try:
        print('Process ',file)
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

        person_mentions = dict(Counter(persons))
        organization_mentions = dict(Counter(organizations))

        df_out = pd.DataFrame.from_dict((sorted(person_mentions, key=person_mentions.get, reverse=False)[:100])).rename(columns={0: 'Person'})
        df_out['Organization']= sorted(organization_mentions, key=organization_mentions.get, reverse=False)[:100]

        print('Save ranking.')
        timestamp = file.split('.')[0].split('_')[-1]
        surname = person.split(' ')[-1]
        df.to_csv(output_directory + '/ranking_' + surname + '_' + timestamp + '.csv')


# Define daily retrieval and filterting as process
class Worker(mp.Process):

    def __init__(self,job_queue):

        super().__init__()

        # Initialize one attribute for worker (job_queue equals parameters of retrieve_GKG_day function)
        self._job_queue = job_queue

    # Define method
    def run(self):

        success_rates = []
        while True:

            # Get paramters from queue
            params = self._job_queue.get()

            # Stop if no dates left
            if len(params) == 0:
                break

            # Else: retrieve GKG daily file
            create_ranking_file(params)

if __name__ == "__main__":

    ########################
    ### input parameters ###
    ########################

    input_directory = "/Users/lucaslinden/Pythonkurs/GKG_Daten"
    output_directory = "/Users/lucaslinden/Pythonkurs/Ranking"
    person = 'joe biden'
    active_cores = mp.cpu_count()-3

    # Get relevant dates
    files = os.listdir(input_directory)

    # Initialize empty job list and empty queue
    jobs = []
    job_queue = mp.Queue()

    for i in range(active_cores):
        p = Worker(job_queue)
        jobs.append(p)
        print('Start Worker ', i+1)
        p.start()

    # Put job into queue
    for file in files:
        job_queue.put({'input_directory': input_directory,
                       'output_directory':output_directory,
                       'person': person,
                       'file': file
                       })

    # Stop if all dates in queue (therefore append lists with none)
    for j in jobs:
        job_queue.put([])

    for job in jobs:
        p.join()
