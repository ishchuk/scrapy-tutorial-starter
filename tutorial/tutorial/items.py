from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose

def remove_quotes(text):
    #strip unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text

class QuoteItem(Item):
    quote_content = Field(input_processor=MapCompose(remove_quotes))
    tags = Field()
    author_name = Field()
    author_birthday = Field()
    author_bornlocation = Field()
    author_bio = Field()
