import scrapy
from craigslist.items import CraigslistItem

class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "http://sfbay.craigslist.org/search/sfc/apa"
    ]

    def parse(self, response):

        for sel in response.xpath("//div[@class='content']/span[@class='rows']/p"):

            item = CraigslistItem()
            item['title'] =  sel.xpath("span/span/a[@class='hdrlnk']").extract()[0]
            item['link']  =  sel.xpath("span/span/a[@class='hdrlnk']/@href").extract()[0]
            yield item
