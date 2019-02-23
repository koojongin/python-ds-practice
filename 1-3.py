import pandas as pd
import numpy as np

CCTV_PATH = './data/seoul-cctv-data.csv'
POPULATION_PATH = './data/seoul-population-data.xls'

# 데이터 리스트 생성 방식중 하나(Series)
dataset = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range('20130101', periods=6);

# print(dates);

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# print(df.index);
# print(df.values);
# print(df.info())
# print(df.describe())
# print(df.sort_values(by='B', ascending=False))
# print(df['A']);
# print(df[0:3]);
# print(df['20130103','20130105']);
# print(df.loc[dates[0]]);
# print(df.loc[:, ['A', 'B']]);
# print(df)
print(df.iloc[3]);
