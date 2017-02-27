import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup as bs
from DoubanMovie.items import DoubanmovieItem


class Spider(scrapy.Spider):

    name = 'douban'
    allowed_domains = ['movie.douban.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        bash1 = '?start='
        for i in range(0, 10):
            url = 'https://movie.douban.com/top250'
            url = url + bash1 + str(i * 25)
            yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanmovieItem()
        group1 = bs(response.text, 'lxml').find_all('div', class_='item')
        for each in group1:
            item['ranking'] = each.find('em').get_text()
            item['movie_name'] = each.find('div', class_='hd').find_all('span', class_='title')[0].get_text()
            temp = each.find('div', class_='bd')
            item['score'] = temp.find('span', class_='rating_num').get_text()
            item['score_num'] = temp.find_all('span')[3].get_text()[:-3]
            print(item)
            yield item


