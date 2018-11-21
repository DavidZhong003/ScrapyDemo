from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from logging import getLogger
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from selenium.webdriver.support import expected_conditions as EC


class SeleniumMiddleware(object):
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.PhantomJS(service_args=service_args)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        pass

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
        return s

    def process_request(self, request, spider):
        """
        PhantomJs 获取界面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug('PhantomJs start working')
        page = request.meta.get('page', 1)
        try:
            self.browser.get(url=request.url)
            self.wait.until(lambda browser: browser.find_element_by_name('contentFrame'))
            # self.logger.info('=====================')
            self.browser.switch_to.frame(self.browser.find_element_by_name('contentFrame'))
            # self.logger.info(self.browser.page_source)
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request,
                                encoding='utf-8', status=200)
            pass
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
