import pandas as pd

with open('corpus_all/basic_results_SS_reasoning.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('SS_basic.csv', encoding='utf-8', index=False)