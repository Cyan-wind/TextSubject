import requests
import re
import csv

#爬取数据
url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
response = requests.get(url,headers = headers)
data = response.text

#爬不到，可能有反爬虫，本地创建txt文件复制粘贴
file = open('D:/data.txt', 'r')
data = file.readlines()
file.close()

#用正则爬出所需数据
pattern1 = re.compile('"isin": "(.*?)"',re.S)
ISIN = re.findall(pattern1,str(data))

pattern2 = re.compile('"bondCode": "(.*?)"',re.S)
Bond_Code = re.findall(pattern2,str(data))

pattern3 = re.compile('"entyFullName": "(.*?)"',re.S)
Issuer = re.findall(pattern3,str(data))

pattern4 = re.compile('"bondType": "(.*?)"',re.S)
Bond_Type = re.findall(pattern4,str(data))

pattern5 = re.compile('"issueStartDate": "(.*?)"',re.S)
Issue_Date = re.findall(pattern5,str(data))

pattern6 = re.compile('"debtRtng": "(.*?)"',re.S)
Latest_Rating = re.findall(pattern6,str(data))

#做一个转置，写入csv
transposed_lists = zip(ISIN, Bond_Code, Issuer,Bond_Type,Issue_Date,Latest_Rating)#做一个转制
with open('D:/data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ISIN', 'Bond_Code', 'Issuer','Bond_Type','Issue_Date','Latest_Rating'])
    writer.writerows(transposed_lists)
file.close()
