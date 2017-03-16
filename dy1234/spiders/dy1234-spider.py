from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from dy1234.items import *


# class DY1234Spider(CrawlSpider):

#     name = 'dy1234'
#     allowed_domains = ['idyjy.com']
#     start_urls = ['http://www.idyjy.com']
#     # start_urls = ['http://www.idyjy.com/sub/23182.html']
#     rules = [Rule(LinkExtractor(allow=['/sub/\d+\.html']),
#                   callback='parse_torrent')]

#     def parse_torrent(self, response):
#         tt = urlItem()
#         tt['url'] = response.url
#         tt['description'] = response.xpath(
#             "//h1/span[@id='name']/text()").extract()
#         yield tt
#         for tt in response.xpath("//ul/li/input[@class='down_url']"):
#             torrent = TorrentItem()
#             torrent['title'] = tt.xpath('@file_name').extract()
#             torrent['link'] = tt.xpath('@value').extract()
#             # torrent['description'].append(description)
#             # print '[+]%s' % (title)
#             # print '[+]%s' % (link)
#             yield torrent

##########################################################################
class DY1234Spider(CrawlSpider):

    name = 'dy1234'
    allowed_domains = ['idyjy.com']
    start_urls = ['http://www.idyjy.com/sub/23182.html']

    def parse(self, response):
        tt = urlItem()
        tt['url'] = response.url
        tt['description'] = response.xpath(
            "//h1/span[@id='name']/text()").extract()
        yield tt
        for tt in response.xpath("//ul/li/input[@class='down_url']"):
            torrent = TorrentItem()
            torrent['title'] = tt.xpath('@file_name').extract()
            torrent['link'] = tt.xpath('@value').extract()
            # print '[+]%s' % (title)
            # print '[+]%s' % (link)
            yield torrent
