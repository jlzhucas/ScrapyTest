# Scrapy settings for scrapy_test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy_test'

SPIDER_MODULES = ['scrapy_test.spiders']
NEWSPIDER_MODULE = 'scrapy_test.spiders'

ITEM_PIPELINES = ['scrapy_test.pipelines.MySQLPipeline',]

MySQL_SERVER = "localhost"
MySQL_DB = "isbullshit"
MySQL_USER = "root"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_test (+http://www.yourdomain.com)'
