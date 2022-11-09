import os
import pandas as pd
from collections import Counter

input_path = "/Users/lucaslinden/Pythonkurs/Ranking/biden"

files = os.listdir(input_path)

organizations = []
persons = []
for file in files:

    # read data
    df = pd.read_csv(input_path + '/' + file)
    organizations += df.Organization.values.tolist()
    persons += df.Person.values.tolist()

final_ranking = pd.DataFrame()
final_ranking['Person'] = list(dict(Counter(persons).most_common(10)).keys())
final_ranking['Organization'] = list(dict(Counter(organizations).most_common(10)).keys())
