import pandas as pd
from openpyxl import load_workbook

class DoExcel():

    def __init__(self):
        pass

    def create_xlsx(df,sheetname):
        df.to_excel('data.xlsx',sheet_name = sheetname)

    def read_sheet(url,sheetname):
        df = pd.read_excel(url,sheet_name=sheetname)
        return df


    def save2sheet(df,url='data.xlsx',filename='data'):
        
        book = load_workbook(url)
        writer=pd.ExcelWriter(url,engine='openpyxl')
        writer.book = book
        df.to_excel(writer,filename)
        writer.save()
