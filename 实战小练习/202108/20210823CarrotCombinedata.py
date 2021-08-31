# -*- coding: utf-8 -*-
# @Date    : 2021年8月23日10:02:35
# @Author  : 花生 lyyjyll@163.com


import pandas as pd
import pathlib2 as pl2

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', None)

data_path = pl2.Path('./data')#当前路径
dfs = (pd.read_excel(d) for d in data_path.glob('*.xls'))#读取所有Excel文件
data = pd.concat(dfs)#合并数据
data.tail(5)
data.drop_duplicates(inplace=True)#去重
print("每列的空缺值数量\n",data.isnull().sum())
data.dropna(how = 'all',subset=['Authors'],axis=0,inplace=True)#去除空值
data.reset_index(inplace=True)
data.to_csv('data.csv')


