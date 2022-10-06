from scrapy.spiders import CrawlSpider, Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from ..items import BookItem

class BookScraperSpider(Spider):
    name = 'simple_bookscraper'
    # start_urls = ['http://books.toscrape.com/index.html']
    start_urls = ['http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html']

    # rules = (
    #     Rule(LinkExtractor(restrict_css='.product_pod > h3 > a'), callback='crawl_book_info'),
    # )

    def parse(self, response):
        book_item = BookItem()

        book_item['title'] = response.css('.col-sm-6.product_main > h1::text').extract()
        book_item['description'] = response.css('.product_page > p::text').extract()
        book_item['price'] = response.css('.price_color::text').extract()

        img_url = response.css('.item.active > img::attr(src)').extract()
        book_item['image_url'] = 'http://books.toscrape.com/' + img_url[0].split('..')[-1]
        response.css('.item.active > img::attr(src)').extract()

        book_item['upc'] = response.css('.table.table-striped > tr:nth_child(1) > td::text').extract()
        book_item['product_type'] = response.css('.table.table-striped > tr:nth_child(2) > td::text').extract()
        book_item['tax'] = response.css('.table.table-striped > tr:nth_child(5) > td::text').extract()
        book_item['available'] = response.css('.table.table-striped > tr:nth_child(6) > td::text').extract()
        book_item['url'] = response.url

        yield book_item
