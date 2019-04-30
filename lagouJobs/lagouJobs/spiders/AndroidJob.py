import scrapy
from scrapy import Request


# 使用selenium 中间件来处理
class AndroidJob(scrapy.Spider):
    name = "androidJob"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com/jobs/list_Android?labelWords=&fromSearch=true&suginput="
    ]

    def parse(self, response):
        pass
