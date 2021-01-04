# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class BatdongsancrawlerPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'rioro1611' # your password
        database = 'batdongsan.com'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
        
    def process_item(self, item, spider):
        self.cur.execute("insert into batdongsan_content(title,area,location,price) values(%s,%s,%s,%s)",(item['title'],item['area'],item['location'],item['price']))
        self.connection.commit()
        return item