import os
import pandas as pd
import jieba
import time

def AddSkills(df, DictPath):
    # ----匯入自定義字典----
    jieba.load_userdict(DictPath)
    # ----建立Skill list，並將自定義字典內的skill加入Skill list
    SkillsList = list()
    with open(DictPath, 'r', encoding='utf-8') as f:
        SkillsList += f.read().upper().split('\n')
        # for skill in f.read().split('\n'):
        #     df[skill] = 0


    for n ,content in enumerate(df['條件要求']):
        content = content.replace(' ','').upper() # 將內文多於空白消除 ,upper => 將字母都轉成大寫
        contentcut = jieba.cut(content)
        WordList = [ w for w in contentcut ] # 將jieba斷字放入list
        # print(wordList)
        for each_word in WordList:
            #---- 判斷jieba的每個斷字是否在SkillsList----
            if each_word in SkillsList:
                if each_word not in df.columns: # 判斷df的欄位是否有skill的欄位
                    df[each_word] = 0
                df.loc[n, each_word] = 1
    return df

if __name__ == "__main__":
    DictPath = './mydict.txt'
    df = pd.read_csv('./資料科學家20210224_1003.csv', encoding='utf-8') # 使用DataFrame讀取CSV資料
    finaldf = AddSkills(df, DictPath)
    testpath = './test' + time.strftime('%Y%m%d_%H%M') + '.csv'
    finaldf.to_csv(testpath, encoding='utf-8-sig') # 編碼方式用'utf-8-sig' 用EXCEL開啟CSV部會出現亂碼




