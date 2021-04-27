import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import jieba
import os


def ETL_104(search, page, isnew):
    # ----製做 DataFrame----
    df_tmp = pd.DataFrame(columns=['公司名稱', '職務名稱', '工作內容', '條件要求', '工作待遇', '福利制度', '網址連結'])  # 暫時存放
    df = pd.DataFrame(columns=['公司名稱', '職務名稱', '工作內容', '條件要求', '工作待遇', '福利制度', '網址連結']) # 主要DF

    # ----104搜尋結果所顯示的最大範圍是3000筆職缺(分成每頁20筆職缺，共150頁)-------
    while page < 150:
        # ------ 製做爬蟲網址物件-------
        Url = 'https://www.104.com.tw/jobs/search/?keyword={}&page={}&isnew={}'.format(search, page, isnew)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }
        # ---使用TryException配合迴圈，當網頁請求失敗時，則會再重新進行requests----
        try:
            res = requests.get(Url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            TotalJobs = soup.select('article[class="b-block--top-bord job-list-item b-clearfix js-job-item"]')

            for n, job in enumerate(TotalJobs):
                CompanyName = job['data-cust-name']  # 公司名稱
                JobName = job.select('a')[0].text  # 職務名稱
                JobUrl = 'https:' + job.select('a')[0]['href']  # 工作內容相關網址
                JobUrl = JobUrl.replace('www', 'm')  # 將網址的 www改為 m
                Job_res = requests.get(JobUrl, headers=headers)  # 對職務網址進行爬蟲
                Job_soup = BeautifulSoup(Job_res.text, 'html.parser')

                # ----工作內容----
                JobContent = Job_soup.select('div.content')[1].text
                JobContent =JobContent.replace('\n', '').replace('\r', '').replace('\t', '').strip()


                # ----薪資待遇及福利----
                JobSalary = Job_soup.select('div.content')[2].text.split('：')[1]
                JobSalary = JobSalary.replace('\n', '').strip() # 調整格式 , strip() => 消除字串前後空白
                EmployeeBenefit = Job_soup.select('div.content')[3].text
                EmployeeBenefit = EmployeeBenefit.strip() #調整格式

                # ----條件要求----
                JobRequires = Job_soup.select('div.content')[5].text
                JobRequires = JobRequires.replace('\n','').strip() # 調整格式

                # 將 '公司名稱'、'職務名稱'、'工作內容'、'條件要求'、'薪資待遇'、'福利制度'、'網址連結' 放入暫時的DataFrame內
                df_tmp.loc[n] = [CompanyName, JobName, JobContent, JobRequires, JobSalary, EmployeeBenefit, JobUrl]
                time.sleep(1)

            df = df.append(df_tmp)  # 將當頁爬蟲的DF加到主要DF
            df_tmp = df_tmp.drop(index=df_tmp.index)  # 將暫存在Dataframe內的資料清空，避免重複加入(筆數少於20時)
            print(len(TotalJobs))  # 查看當頁的資料筆數
            print('======================第{}頁結束====================='.format(page))
            page += 1

            #----若當頁職缺未超過20筆，代表沒有下一頁，即可跳出迴圈----
            if len(TotalJobs) < 20:
                break
        except:
            print('Retry')
            time.sleep(30)

    df = df.reset_index(drop=True)  # 將index 重新排序
    return df


