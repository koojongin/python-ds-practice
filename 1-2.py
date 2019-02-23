import pandas as pd

CCTV_PATH = './data/seoul-cctv-data.csv'
POPULATION_PATH = './data/seoul-population-data.xls'

cctv = pd.read_csv(CCTV_PATH, encoding='utf-8')
population = pd.read_excel(POPULATION_PATH, encoding='utf-8')

# define functions
def get_head(csv):
    return csv.head()

# 컬럼 파싱
cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)

# 엑셀 파일 읽기 + 컬럼 파싱
pop = pd.read_excel(POPULATION_PATH, header=2, parse_cols='B,D,G,J,N', encoding='utf-8')
pop = pop.rename(columns={
    pop.columns[0]: '구별',
    pop.columns[1]: '인구수',
    pop.columns[2]: '한국인',
    pop.columns[3]: '외국인',
})

print(pop);