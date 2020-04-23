from scrapy.item import Item, Field

class QuoteItem(Item):
    quote_content = Field()
    tags = Field()
    author_name = Field()
    author_birthday = Field()
    author_bornlocation = Field()
    author_bio = Field()
    