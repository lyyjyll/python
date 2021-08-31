# -*- coding: utf-8 -*-
# @Date    : 2021年8月23日10:05:35
# @Author  : 花生 lyyjyll@163.com
# pandas=1.3.1

import pandas as pd

df = pd.read_csv('./savedrecs.txt',encoding='utf-8',sep='\t')
print("PY空缺值为：",df['PY'].isnull().sum())
df.dropna(subset = ['PY'],how='all',axis=0,inplace=True)
print("Now PY空缺值为：",df['PY'].isnull().sum())
df.drop_duplicates(inplace=True)
df.PD = df.PD.astype('int')
print(df.PD.head())
#print(df.info())


df.to_csv('datatsv.tsv',sep='\t')
