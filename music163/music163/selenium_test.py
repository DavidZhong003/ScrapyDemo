from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def stat_test(url="http://www.baidu.com"):
    # driver = webdriver.Chrome('/Users/zhongshan/Downloads/chromedriver')
    driver = webdriver.PhantomJS()
    driver.get(url=url)
    print(driver.title)
    # print(driver.page_source)
    iframe = driver.find_element_by_xpath('//*[@id="g_iframe"]')
    print(iframe)
    driver.switch_to.frame(iframe)
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    stat_test("https://music.163.com/#/discover/artist")
