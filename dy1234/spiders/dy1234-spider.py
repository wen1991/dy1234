from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from dy1234.items import *

# import MySQLdb

import logging

logger = logging.getLogger('mycustomlogger')


class DY1234Spider(CrawlSpider):
    name = 'dy1234'
    allowed_domains = ['idyjy.com']
    start_urls = ['http://www.idyjy.com']
    # start_urls = ['http://www.idyjy.com/sub/23182.html']
    rules = [Rule(LinkExtractor(allow=['/sub/\d+\.html']),
                  callback='parse_torrent')]
    id_num = 0

    def parse_torrent(self, response):
        tt = urlItem()
        self.id_num = self.id_num + 1
        logger.info("[id]=%d" % self.id_num)
        logger.info("[url]=%s" % response.url)
        tt['url'] = response.url
        tt['description'] = response.xpath(
            "//h1/span[@id='name']/text()").extract()
        yield tt
        for tt in response.xpath("//ul/li/input[@class='down_url']"):
            torrent = TorrentItem()
            torrent['title'] = tt.xpath('@file_name').extract()
            torrent['link'] = tt.xpath('@value').extract()
            yield torrent

##########################################################################
# class DY1234Spider(CrawlSpider):

#     name = 'dy1234'
#     allowed_domains = ['idyjy.com']
#     start_urls = ['http://www.idyjy.com/sub/23182.html']

#     def parse(self, response):
#         tt = urlItem()
#         tt['url'] = response.url
#         tt['description'] = response.xpath(
#             "//h1/span[@id='name']/text()").extract()
#         yield tt
#         for tt in response.xpath("//ul/li/input[@class='down_url']"):
#             torrent = TorrentItem()
#             torrent['title'] = tt.xpath('@file_name').extract()
#             torrent['link'] = tt.xpath('@value').extract()
#             # print '[+]%s' % (title)
#             # print '[+]%s' % (link)
#             yield torrent
