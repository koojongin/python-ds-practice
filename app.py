import pandas as pd
import logging

CCTV_PATH = './data/seoul-cctv-data.csv'
POPULATION_PATH = './data/seoul-population-data.xls'

cctv = pd.read_csv(CCTV_PATH, encoding='utf-8')
population = pd.read_excel(POPULATION_PATH, encoding='utf-8')


# define functions
def get_head(csv):
    return csv.head()


cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)

print(get_head(population))
