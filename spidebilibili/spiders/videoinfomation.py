# -*- coding: utf-8 -*-
import scrapy,json,time


class VideoinfomationSpider(scrapy.Spider):
    name = 'videoinfomation'
    allowed_domains = ['bilibili.com']
    # start_urls = ['http://bilibili.com/']

    def start_requests(self):
        # temp_url = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_582220666527276&rid=22&type=0&pn=1&ps=20&jsonp=jsonp&_=1537632504143'
        for page_num in range(1,10):
            url = 'https://api.bilibili.com/x/web-interface/newlist?&rid=22&type=0&pn='+str(page_num)+'&ps=20&jsonp=jsonp&_=1537635939369'
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        for eve in json.loads(response.body.decode('utf-8'))['data']['archives']:
            yield eve
