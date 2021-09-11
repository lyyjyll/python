###从数据源筛选各个地区的ESI数据，并存到新的工作簿中

import pandas as pd
from openpyxl import load_workbook


url = './20210902ESI分学科.xlsx'


def province_data(df,url,province):
    df = df.loc[df['省份']==province]
    df.reset_index(inplace=True,drop=True)
    print(df.head(5))
    book = load_workbook(url)
    writer=pd.ExcelWriter(url,engine='openpyxl')
    writer.book = book
    df.to_excel(writer,province)
    writer.save()

df_dalu = pd.read_excel(url,sheet_name='大陆')

province = ['北京','上海']

for pro in province:
    province_data(df_dalu,url=url,province=pro)

