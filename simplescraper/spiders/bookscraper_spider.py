from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BookScraperSpider(CrawlSpider):
    name = 'simplescraper'
    # start_urls = ['http://books.toscrape.com/index.html']
    start_urls = ['http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html']

    # rules = (
    #     Rule(LinkExtractor(restrict_css='.product_pod > h3 > a'), callback='crawl_book_info'),
    # )

    def crawl_book_info(self, response):
        book_item = BookItem()

        book_item['title'] = response.css('.product_main > h1::text').extract()
        # book_item['description'] = response.css('#product_description > p::text').extract()
        # book_item['price'] = response.css('.price_color::text').extract()
        # book_item['image_url'] = response.urljoin(response.css('.item-active > img::attr(src)').extract())
        # book_item['upc'] = response.css('.table.table-striped > tr::nth_child(1) > td::text').extract()
        # book_item['prod_type'] = response.css('.table.table-striped > tr::nth_child(2) > td::text').extract()
        # book_item['tax'] = response.css('.table.table-striped > tr::nth_child(5) > td::text').extract()
        # book_item['available'] = response.css('.table.table-striped > tr::nth_child(6) > td::text').extract()
        # book_item['url'] = response.url

        yield book_item
