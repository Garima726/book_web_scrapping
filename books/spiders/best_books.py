import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestBooksSpider(CrawlSpider):
    name = "best_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rules = [Rule(LinkExtractor(restrict_xpaths="//ol[@class='row']/li/article"), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths="//ul[@class='pager']/li[position() = last()]/a"))
             ]
             

    def parse_item(self, response):
       yield{
           'book_name': response.xpath(".//h3/a/text()").get(),
            'price': response.xpath(".//div[@class='product_price']/p[@class='price_color']/text()").get(),
            'url': response.xpath(".//div[@class='image_container']/a/@href").get()
       }