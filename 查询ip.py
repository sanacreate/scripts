# 在ip-api.com上查询ip地址，一分钟限制在45次，这里30次，2s最多一次，把ip地址提取出来就行
from requests import get
import json
import re

aim_ip = ""
response = get('http://ip-api.com/json/'+ aim_ip).text
print(response)
#查询ip地址

xx = """
"""

x = []

def find_ip(x:str):
    pattern = r'Failed password.*?from (.*?) port'
    return re.findall(pattern, x)

def ask_ip(x:list):
    for i in x:
        response = get('http://ip-api.com/json/'+i).text
        print(response)
print(find_ip(xx))

