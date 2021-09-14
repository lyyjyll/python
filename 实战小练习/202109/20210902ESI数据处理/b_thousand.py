###筛选接近各地区学科ESI接近千分之一的学校（0.1~0.2个学科数）

import pandas as pd
from openpyxl import load_workbook


url = './20210902ESI分学科.xlsx'

def read_pro_data(url, pro):
    df = pd.read_excel(url,sheet_name=pro)
    return df

def thousand(df,dis_name,dis_count):
    df_new = []
    for dis,count in zip(dis_name,dis_count):
        df_dis = df.loc[df['学科'] == dis]
        df_appro = df_dis.loc[(df_dis['ESI序']>(count*0.1)) & (df_dis['ESI序']<=(count*0.2))]
        df_new.append(df_appro)
    df_end = pd.concat(df_new)
    df_end.reset_index(inplace=True,drop=True)
    return df_end
    

def save_to_sheet(df,url,location):
    sheet_name = location +'接近千分之一'
    book = load_workbook(url)
    writer=pd.ExcelWriter(url,engine='openpyxl')
    writer.book = book
    df.to_excel(writer,sheet_name)
    writer.save()
    

def main():

    prolist = ['北京','上海','江苏']



    df_jiangsu = read_pro_data(url,prolist[2])
    displine_list = ['农业科学', '生物学与生物化学', '化学', '临床医学', '计算机科学', '经济学与商务学','工程学', '环境生态学', '地质学', '免疫学', '材料科学', '数学', '微生物学', '分子生物学与遗传学','交叉学科', '神经科学与行为学', '药理学与毒理学', '物理学', '植物学与动物科学','精神病学与行为学', '社会科学','空间科学']
    jiangsu_dis_hundred_count = [981,1230,1478,5103,580,397,1805,1342,840,876,1056,301,557,932,148,1007,1035,789,1459,832,1780,184]


    df_thousand = thousand(df_jiangsu,dis_name=displine_list,dis_count=jiangsu_dis_hundred_count)
    print(df_thousand.head(20))
    save_to_sheet(df_thousand,url=url,location=prolist[2])

if __name__ == '__main__':
    main()
