# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb
from scrapy.exception import DropItem
from scrapy.conf import	settings
from scrapy import log


class MySQLPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host=settings['MySQL_SERVER'], user=settings['MySQL_USER'], db=settings['scrapy_test'], charset='utf-8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            # here we only check if the data is not null
            # but we could do any crazy validation we want
            if not data:
                valid = False
                raise DropItem("Missing %s of blogpost from %s" % (data, item['url']))
        if valid:
            self.cursor.execute()
            self.conn.commit()
            self.cursor.close()
            log.msg("Item wrote to MySQL database",
                    level=log.DEBUG, spider=spider)
        return item
