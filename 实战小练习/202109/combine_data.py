import pandas as pd
from pandas.core.reshape.concat import concat
import pathlib2 as pl2



datadf = []
year_list = list(range(2016,2021))
for year,xls in zip(year_list, pl2.Path('./20210901_data').glob('*.xls')):
    df = pd.read_excel(xls)
    df = df.iloc[1:32,:]
    df.columns = df.iloc[0].tolist()
    df = df.iloc[1:,:]
    df.reset_index(inplace=True)
    df['year'] = year
    datadf.append(df)

df = concat(datadf,axis=0)
df.reset_index(inplace=True)
df.drop(columns=['level_0','index'],inplace=True)
df.to_csv('data_combine.csv')
print(df.head(5))




