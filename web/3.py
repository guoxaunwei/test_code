'''
    断言本身就是用来校验正确性的，你如果把错误给处理了，请问你怎么去知道对不对呢？
    断言本质上是预期结果与实际结果的匹配，那这个匹配当然是在最后再匹配的。
    在UI自动化中，断言是对流程的最终结果进行校验即可。中途可以通过显式等待做一些基本的校验，但是不推荐。
    自动化测试在一些特定情况下需要考虑到清理脏数据的操作。
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
driver.find_element('name', 'accounts').send_keys('xuzhu666')
driver.find_element('name', 'pwd').send_keys('123456')
driver.find_element('xpath', '//button[text()="登录"]').click()
# 获取退出按钮的文本
# 校验文本是否符合预期结果
assert driver.find_element('link text', '退出').text == '退出1', '断言失败'

