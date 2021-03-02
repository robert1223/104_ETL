from ETL import ETL_104
import os
import time
from Skills import AddSkills

# ------將 DataFrame資料寫入CSV------------
# 給予兩個參數，"檔案名稱"及"DataFrame"
def CreateData(DataName, df):
    path = './' + DataName + time.strftime('%Y%m%d_%H%M') + '.csv'
    df.to_csv(path, encoding='utf-8-sig')


if __name__ == "__main__":
    search = "資料科學家"  # 職缺名稱
    isnew = 30  # 最近日期
    page = 1 # 起始頁數
    DictPath = './mydict.txt'
    df = ETL_104(search,page,isnew)
    finaldf = AddSkills(df, DictPath)
    CreateData(search, finaldf)
    print('Done')