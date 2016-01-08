import scrapy

from hello.items import DmozItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class HelloSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["9900.la"]
    base_url = 'http://9900.la/html/tupian/yazhousetu/'
    start_urls = [
       "http://9900.la/html/tupian/yazhousetu/index.html"
    ]

    rules = (
        Rule(LinkExtractor(allow=('[0-9]+\.html', )), callback='parse_item'),
    )


    def parse_item(self, response):
        item = DmozItem()
        r = response.xpath('//ul/li')
        print r
        for e in r:
            item['link'] = response.xpath('//a/@href').extract()
            item['image_urls'] = response.xpath('//img/@src').extract()
            yield item
