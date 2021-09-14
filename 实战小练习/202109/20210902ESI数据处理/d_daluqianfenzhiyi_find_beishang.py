import pandas as pd
from c_shanghaibeijing_thousand import save_to_sheet,read_data

def filter_province(df,pro):
    df_pro = df.loc[df['省份']==pro]
    df_pro.reset_index(inplace=True,drop=True)
    return df_pro

def main():
    url = '20210902ESI分学科.xlsx'
    df = read_data(url,'大陆千分之一')
    pro_list = ['北京','上海','江苏']
    for pro,filename in zip(pro_list,pro_list):
        save_to_sheet(filter_province(df,pro),url,filename+'千分之一')
        print('***'*4+'Success打印{file}千分之一'.format(file=filename)+'***'*4)


if __name__ == '__main__':
    main()

