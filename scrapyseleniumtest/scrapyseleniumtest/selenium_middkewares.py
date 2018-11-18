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
            self.browser.get(request.url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
                submit = self.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
                input.clear()
                input.send_keys(page)
                submit.click()
            self.wait.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist items.item')))

            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request,
                                encoding='utf-8', status=200)
            pass
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
