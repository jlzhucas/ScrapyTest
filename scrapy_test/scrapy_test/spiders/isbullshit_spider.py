# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector

# from scrapy_test.items import DmozItem

# class DmozSpider(BaseSpider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]

#     def parse(self, response):
#         hxs = HtmlXPathSelector(response)
#         sites = hxs.select('//ul/li')
#         items = []
#         for site in sites:
#             item = DmozItem()
#             item['title'] = site.select('a/text()').extract()
#             item['link'] = site.select('a/@href').extract()
#             item['desc'] = site.select('text()').extract()
#             items.append(item)
#         return items

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractor.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from isbullshit.items import IsBullshitItem

class IsBullshitSpider(CrawlSpider):
    name = 'isbullshit'
    start_urls = ['http://isbullsh.it'] # urls from which the spider will start crawling
    rules = [Rule(SgmlLinkExtractor(allow=[r'page/\d+']),follow=True),
        # r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
        Rule(SgmlLinkExtractor(allow=[r'\d{4}/\d{2}\w+']), callback='parse_blogpost')]
        # r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs

    def parse_blogpost(self, response):
        hxs = HtmlXPathSelector(response)
        item = IsBullshitItem()
        # Extract title
        item['title'] = hxs.select('//header/h1/text()').extract()  # XPath selector for title
        item['tag'] = hxs.select("//header/div[@class='post-data']/p/a/text()").extract()   # Xpath selector for tag(s)
        return item


