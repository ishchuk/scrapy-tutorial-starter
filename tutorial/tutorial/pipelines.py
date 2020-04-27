# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from models import Quote, Author, Tag, db_connect, create_table
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class SaveQuotesPipeline(object):
    def __init__(self):
        """initialises database connections and creates tables"""
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """saves quotes in the database; this method gets called for every single item pipeline component"""
        session = self.Session()
        quote = Quote()
        author = Author()
        tag = Tag()
        author.name = item['author_name']
        author.birthday = item['author_birthday']
        author.bornlocation = item['author_bornlocation']
        author.bio = item['author_bio']
        quote.quote_content = item['quote_content']

        #check whether the author exists
        exist_author = session.query(Author).filter_by(name = author.name).first()
        if exist_author is not None:
            quote.author = exist_author
        else:
            quote.author = author

        #check wheher this quote has tags on it
        if 'tags' in item:
            for tag_name in item['tags']:
                tag = Tag(name = tag_name)
                exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                if exist_tag is not None:
                    tag = exist_tag
                quote.tags.append(tag)

        try:
            session.add(quote)
            session.commit()
        
        except:
            session.rollback()
            raise
            
        finally:
            session.close()

        return item