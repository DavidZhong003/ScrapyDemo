import scrapy
from scrapy import Request


class AndroidJob(scrapy.Spider):
    name = "android"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com/jobs/list_Android?labelWords=&fromSearch=true&suginput="
    ]

    def parse(self, response):
        pass
