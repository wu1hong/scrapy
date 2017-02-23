# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.23us.com/book/67054'
response = requests.get(url)
#print(response.encoding)
response.encoding = 'gbk'

#a = BeautifulSoup(response.text, 'lxnl').find('table').find_all('td')[2].get_text().strip()
b = '/2622'
if b.find('/') == 0:
    b = b.replace('/', '')
print(b)

