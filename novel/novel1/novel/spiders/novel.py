import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
import sys
import os
sys.path.append(os.path.abspath('..'))
from items import NovelItem



class MySpider(scrapy.Spider):

    name = 'novel'
    allowed_domains = ['23us.com']
    bash_url = 'http://www.23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find('a', class_='last').get_text()
        bashurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + '.html'
            yield Request(url, callback=self.get_name, encoding='gbk')

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novel_name = td.find('a').get_text()
            novel_url = td.find('a')['href']
            yield Request(novel_url, callback=self.get_chapterurl, meta={'name': novel_name,'url': novel_url},
                          encoding='gbk')

    def get_chapterurl(self, response):
        item = NovelItem()
        item['name'] = str(response.meta['name'])
        item['novel_url'] = str(response.meta['url'])
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text().strip()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url[-6:-1])
        if name_id.find('/') == 0:
            name_id = name_id.replace('/', '')
        serial_status = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[2].get_text().strip()
        serial_number = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[4].get_text().strip()
        item['category'] = str(category)
        item['author'] = str(author)
        item['name_id'] = str(name_id)
        item['serial_status'] = str(serial_status)
        item['serial_number'] = str(serial_number)
        yield item

if __name__ == '__main__':
    print(sys.path)

