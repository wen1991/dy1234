from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


from dy1234.items import *

# import MySQLdb

# class DY1234Spider(scrapy.Spider):
#     name = 'author'

#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         # follow links to author pages
#         for href in response.css('.author + a::attr(href)').extract():
#             yield scrapy.Request(response.urljoin(href),
#                                  callback=self.parse_author)

#         # follow pagination links
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).extract_first().strip()

#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }


class DY1234Spider(scrapy.Spider):
    name = 'dy1234'
    allowed_domains = ['idyjy.com']

    domain = 'http://www.idyjy.com'
    # start_urls = ['http://www.idyjy.com/sub/23182.html']
    id_num = 0

    def start_requests(self):
        urls = []
        for i in range(1, 620):
            url = 'http://www.idyjy.com/w.asp?p=' + str(i) + '&f=3&l=s'
            self.log('[start_requests]%s' % url)
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        imgs = response.xpath(
            "//a[@class='play-img']")
        # self.log('[parse]:%s' % imgs.xpath('@href').extract())
        for img in imgs:
            # self.log('[parse]:%s' % img.xpath('@href').extract()[0])
            url = self.domain + img.xpath('@href').extract()[0]
            self.log('[parse]:%s' % url)
            yield scrapy.Request(url=url, callback=self.parse_torrent)

    def parse_torrent(self, response):
        for tt in response.xpath("//ul/li/input[@class='down_url']"):
            torrent = TorrentItem()
            torrent['title'] = tt.xpath('@file_name').extract()
            torrent['link'] = tt.xpath('@value').extract()
            yield torrent

##########################################################################
# class DY1234Spider(CrawlSpider):
#     name = 'dy1234'
#     allowed_domains = ['idyjy.com']
#     start_urls = ['http://www.idyjy.com']
#     # start_urls = ['http://www.idyjy.com/sub/23182.html']
#     rules = [Rule(LinkExtractor(allow=['/sub/\d+\.html']),
#                   callback='parse_torrent')]
#     id_num = 0

#     def parse_torrent(self, response):
#         tt = urlItem()
#         self.id_num = self.id_num + 1
#         logger.info("[id]=%d" % self.id_num)
#         logger.info("[url]=%s" % response.url)
#         tt['url'] = response.url
#         tt['description'] = response.xpath(
#             "//h1/span[@id='name']/text()").extract()
#         yield tt
#         for tt in response.xpath("//ul/li/input[@class='down_url']"):
#             torrent = TorrentItem()
#             torrent['title'] = tt.xpath('@file_name').extract()
#             torrent['link'] = tt.xpath('@value').extract()
#             yield torrent

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
