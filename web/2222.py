'''
    鼠标悬停：通过ActionChains类来实现悬停的操作行为。
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
sleep(3)
driver.maximize_window()
driver.get('http://www.baidu.com')
el = driver.find_element('xpath', '//span[text()="设置"]')
# 创建actions对象，进行悬停的操作。固定写法，在悬停的时候，鼠标不要乱动。避免出现问题
actions = ActionChains(driver)
actions.move_to_element(el).perform()
# 百度不是一个好百度。很多系统里会出现有报错，提示元素无法进行click交互
# el.click()
driver.find_element('link text', '搜索设置').click()
# 截图：自己写路径进行文件保存
driver.save_screenshot('./img/1.png')

