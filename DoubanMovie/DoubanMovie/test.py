import requests
from bs4 import BeautifulSoup as bs

url = 'https://movie.douban.com/top250?start=225'
response = requests.get(url)
#print(response.text)
group1 = bs(response.text, 'lxml').find_all('div', class_='item')
for each in group1:
    con = each.find('div', class_='bd').find_all('span')[3].get_text()
    con = con[:-3]
    print(con)
