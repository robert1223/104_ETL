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
        SkillsList += f.read().split('\n')

    # ----將SKillsL做成D字典，在轉成DataFrame用來做欄位對應----
    SkillsDict = [{'name': x, 'Jieba': x.upper()} for x in SkillsList]
    Skill_DF = pd.DataFrame(data=SkillsDict)

    for n ,content in enumerate(df['條件要求']):
        content = content.replace(' ','').upper() # 將內文多於空白消除 ,upper => 將字母都轉成大寫
        contentcut = jieba.cut(content)
        WordList = [ w for w in contentcut ] # 將jieba斷字放入list
        # print(wordList)
        for each_word in WordList:

            #---- 判斷jieba的每個斷字是否在Skill_DF的Jieba欄位內----
            if each_word in Skill_DF['Jieba'].tolist():  # tolist() 把DF欄位的內容轉成 list

                #---- if條件成立後，先抓出所對應的row的index，再根據index去抓name欄位的內容----
                skill_index = Skill_DF[Skill_DF.Jieba == each_word].index.tolist()[0]
                Add_Skill_Column = Skill_DF['name'][skill_index]
                #---- 判斷df的欄位是否有skill的欄位----
                if Add_Skill_Column not in df.columns:
                    df[Add_Skill_Column] = 0
                df.loc[n, Add_Skill_Column] = 1
    return df

if __name__ == "__main__":
    DictPath = './mydict.txt'
    df = pd.read_csv('./資料科學家20210224_1003.csv', encoding='utf-8') # 使用DataFrame讀取CSV資料
    finaldf = AddSkills(df, DictPath)
    SavePath = './test' + time.strftime('%Y%m%d_%H%M') + '.csv'
    finaldf.to_csv(SavePath, encoding='utf-8-sig') # 編碼方式用'utf-8-sig' 用EXCEL開啟CSV部會出現亂碼




