

from selenium import webdriver

path = 'phantomjs.exe'

browser = webdriver.PhantomJS(path)


url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')

import time
time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('昆凌')

time.sleep(3)

browser.save_screenshot('kunling.png')
