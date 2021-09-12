import pandas as pd

url = 'http://www.xiladaili.com/https/'

for table in pd.read_html(url):

    table.to_csv('proxy.csv',mode='a',encoding='utf-8')