import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from batdongsancrawler.items import officeItem
import re

class BatdongsanSpider(scrapy.Spider):
    name = 'batdongsan'
    allowed_domains = ['batdongsan.com.vn']
    def start_requests(self):
        for page in range(1,1000):
            yield self.make_requests_from_url('https://batdongsan.com.vn/cho-thue-van-phong-da-nang/p%s'%page)    
    def parse(self, response):
        subString = 'm2'
        officeItems = response.xpath("//div[@id = 'product-lists-web']/div[@ipos]/a/div[@class = 'product-main']")
        for x in range(0,len(response.xpath("//div[@id = 'product-lists-web']/div[@ipos='1']/a/div[@class = 'product-main']")*1000)):
            item = officeItem()
            tempPrice = ''
            item['title'] =  response.xpath(".//h3[@class= 'product-title']/span/text()").extract()[x].strip()
            tempArea = response.xpath(".//div[@class= 'product-info']/span[@class = 'area']/text()").extract()[x]            
            item['location'] = response.xpath(".//div[@class= 'product-info']/span[@class = 'location']/text()").extract()[x][:-9]
            tempPrice = response.xpath(".//div[@class= 'product-info']/span[@class = 'price']/text()").extract()[x]
            tempIntPrice = ''.join(x for x in tempPrice if x.isdigit())
            tempIntArea = int(tempArea[:-3])
                item['price'] = int(tempIntPrice) * tempIntArea / 1000
            item['area'] = tempIntArea
            if int(tempIntPrice) > 100:
            else: 
                item['price'] = int(tempIntPrice)
            yield item