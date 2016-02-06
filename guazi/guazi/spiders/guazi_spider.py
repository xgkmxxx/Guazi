# coding:utf-8
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from guazi.items import GuaziItem

class GuaziSpider(CrawlSpider):
    name = "guazi"
    allowed_domains = ["www.guazi.com"]
    start_urls = [
        "http://www.guazi.com/www/buy/"
    ]
    #网页url格式为'http://www.guazi.com/www/buy/o2'表示第二页
    rules = [
    Rule(LinkExtractor(allow=("/www/buy/o\d")),
                        follow = True,
                        callback = 'parse_item')
    ] 
    def parse_item(self, response):
        items = []
        #汽车信息在<div class="list-infoBox">下
        for car in response.xpath("//div[@class='list-infoBox']"):
            item = GuaziItem()
            item['name'] = car.xpath(".//a/@title").extract()
            
            item['city'] = car.xpath(".//p[@class='fc-gray']/span[1]/text()").extract()
            
            item['time'] = car.xpath(".//p[@class='fc-gray']/span[2]/text()").extract()
            
            car_mile = car.xpath(".//p[@class='fc-gray']/text()").extract()
            #去掉文字前后的空格
            item['mile'] = ''.join(car_mile).strip()

            car_price = car.xpath(".//p[@class='priType-s']/span[1]/i/text()").extract()
            item['price'] = ''.join(car_price).strip()

            items.append(item)
        return items

