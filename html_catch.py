# 中文网站爬虫，可以解决gbk编码问题
from requests import get
from bs4 import BeautifulSoup
from time import sleep
main_ip = ""
root_ip = ""  
response = get(main_ip)
response.encoding = 'gb2312'
soup = BeautifulSoup(response.text, 'html.parser')
aim = get("")
aim.encoding = 'GBK'
with open("test.html", "w",encoding='GBK' ) as f:
    f.write(aim.text)
son_ip = soup.findAll('tr') 
for i in son_ip:
    try:
        link = root_ip + i.find('a').get('href')
        print(link)
        error_info = str(link)
        title = i.find('a').text
        title = title.strip()
        aim = get(link)
        aim.encoding = 'GBK'
        res = aim.text
        with open(f"{title}.html", "w",encoding='GBK' ) as f:
            f.write(res)
        print("ok")
        print(f"已下载：{title}")
    except Exception as err:
        print(err)
        pass