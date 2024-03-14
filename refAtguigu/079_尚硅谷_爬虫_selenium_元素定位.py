

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位

# 根据id来找到对象
# button = browser.find_element_by_id('su')
# print(button)

# 根据标签属性的属性值来获取对象的
# button = browser.find_element_by_name('wd')
# print(button)

# 根据xpath语句来获取对象
# button = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用的bs4的语法来获取对象
# button = browser.find_elements_by_css_selector('#su')
# print(button)

# button = browser.find_element_by_link_text('直播')
# print(button)