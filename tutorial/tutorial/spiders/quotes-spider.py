import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']
    def parse(self,response):
        #self.logger.info('hello hello there')
        for quote in quotes:
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css('quote_content','.text::text')
            loader.add_css('tags', '.tag::text')
            #author_url = quote.css('.author + a::attr(href)').get()
            self.logger.info('get author page url')
            yield response.follow(author_url, callback = self.parse_author)

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
    def parse_author(self, response):
        yield {
            'author_name': response.css('.author-title::text').get(),
            'author_birthday': response.css('.author-born-date::text').get(),
            'author_bornlocation': response.css('.author-born-location::text').get(),
            'author_bio': response.css('.author-description::text').get(),
        }