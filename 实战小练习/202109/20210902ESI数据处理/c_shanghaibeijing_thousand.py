import pandas as pd
from openpyxl import load_workbook


def read_data(url,sheetname):
    df = pd.read_excel(url,sheet_name=sheetname)
    return df

def filter_thousand(df,dis_name,dis_count):
    #筛选千分之一学科
    df_new = []
    for dis,count in zip(dis_name,dis_count):
        df_dis = df.loc[df['学科'] == dis]
        df_thousand = df_dis.loc[df_dis['ESI序']<=(count*0.1)]
        df_new.append(df_thousand)
    df_end = pd.concat(df_new)
    df_end.reset_index(inplace=True,drop=True)
    df_end.drop(columns=['Unnamed: 0'],inplace=True)
    return df_end


def save_to_sheet(df,url,filename):
    book = load_workbook(url)
    writer=pd.ExcelWriter(url,engine='openpyxl')
    writer.book = book
    df.to_excel(writer,filename)
    writer.save()
    #print('***'*4+'Success打印{file}'.format(file=filename)+'***'*4)

def main():
    url = '20210902ESI分学科.xlsx'
    dis_name = ['农业科学', '生物学与生物化学', '化学', '临床医学', '计算机科学', '经济学与商务学','工程学', '环境生态学', '地质学', '免疫学', '材料科学', '数学', '微生物学', '分子生物学与遗传学','交叉学科', '神经科学与行为学', '药理学与毒理学', '物理学', '植物学与动物科学','精神病学与行为学', '社会科学','空间科学']
    dis_count = [981,1230,1478,5103,580,397,1805,1342,840,876,1056,301,557,932,148,1007,1035,789,1459,832,1780,184]

    df_shanghai = read_data(url,'上海')
    df_beijing = read_data(url,'北京')

    dfbeijing = filter_thousand(df_beijing,dis_name,dis_count)
    dfshanghai = filter_thousand(df_shanghai,dis_name,dis_count)

    save_to_sheet(dfbeijing,url,'北京千分之一')
    save_to_sheet(dfshanghai,url,'上海千分之一')




if __name__ == '__main__':
    main()