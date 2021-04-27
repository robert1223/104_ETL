# 104人力銀行爬蟲
## 此爬蟲透過Python語言做為簡易的爬蟲程式
### 3/2 首次上傳
- 僅給予工作名稱、更新日期、頁數三個簡易參數做查詢(後續若有增加其他查詢參數會將程式碼更新)
- 利用requests對網頁進行請求，再用Beautiful整理html檔
- 將所查到的資料放在DataFrame 包含'公司名稱'、'職務名稱'、'工作內容'、'條件要求'、'薪資待遇'、'福利制度'、'網址連結'
- 新增所需要的skill的自定義字典'mydict.txt'
- 根據DataFrame 內的條件要求進行jieba斷字，並將jieba斷字與字定義字典進行比對，若有相符者在DataFrame新增skill欄位，並將其內容填入1
- 最後再將DataFrame資料轉成csv檔案方便檔案儲存
### 3/6 更新
- 修改'Skills.py'，上個版本所新增的skill欄位都會用大寫的方式新增，這次改版將所新增的欄位按照原本自定義字典'mydict.txt'的內容做新增
- 新增'01-TO_EXCEL.py'檔，可將爬蟲過後的資料儲存成Excel檔案
### 4/27 更新
- 修改檔名 ETL.py => 104_Crawler.py
- 修改檔名 Skills.py => Skill_ Statistics.py
- 新增範例檔 sample20210427_1358.csv
