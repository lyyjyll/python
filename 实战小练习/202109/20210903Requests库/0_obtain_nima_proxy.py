import pandas as pd

url = 'http://www.nimadaili.com/https/'

for table in pd.read_html(url):

    table.to_csv('nima_proxy.csv',mode='a',encoding='utf-8')