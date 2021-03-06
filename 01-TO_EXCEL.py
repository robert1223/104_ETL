from ETL import ETL_104
import time
from xlsxwriter import Workbook
import pandas as pd
from Skills import AddSkills



# ------建立EXCEL檔案，將 DataFrame資料寫入------------
# 給予兩個參數，"檔案名稱"及"DataFrame"
def CreateData(DataName, df):
    path = './' + DataName + time.strftime('%Y%m%d_%H%M') + '.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=DataName, index=False)
    writer.save()

if __name__ == "__main__":
    search = "資料科學家"  # 職缺名稱
    isnew = 30  # 最近日期
    page = 1 # 起始頁數
    DictPath = './mydict.txt'
    df = ETL_104(search, page, isnew)
    finaldf = AddSkills(df, DictPath)
    CreateData(search, finaldf)
    print('Done')


    # # ----印出測試----
    # print(CompanyName,end="  ")
    # print(JobName,end="  ")
    # print(JobUrl)
    # print(Job_soup) # test
    # JobContent = Job_soup.select('div.content') # test
    # print(JobContent) # test
    # print(JobRequires) # test
    # print('=========================================')






