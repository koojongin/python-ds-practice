import pandas as pd
import numpy as np

CCTV_PATH = './data/seoul-cctv-data.csv'
POPULATION_PATH = './data/seoul-population-data.xls'

cctv = pd.read_csv(CCTV_PATH, encoding='utf-8')
population = pd.read_excel(POPULATION_PATH, encoding='utf-8')

print(pop);