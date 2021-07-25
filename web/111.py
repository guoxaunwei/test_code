'''
    网易云音乐的课后作业
    http://music.163.com
'''
from time import sleep

from selenium import webdriver

# 创建webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 访问url
driver.get('http://music.163.com')
driver.maximize_window()
print(driver.window_handles)
# 等待是为了让代码的运行成功率更高
sleep(2)
# 执行登录流程
driver.find_element('xpath', '//*[@id="auto-id-qTpelWTdKT6CgCx6"]/a').click()
sleep(1)
driver.find_element('link text', '选择其他登录模式').click()
driver.find_element('id', 'j-official-terms').click()
driver.find_element('link text', 'QQ登录').click()
# 句柄的处理
'''
    在计算机世界中，不同的标签页，是通过不同的字符串来区分。可以理解为id，统一称之为句柄
    通过selenium操作的标签页，在不切换的情况下，只会一直聚焦在第一个页面。
    如果要操作新的句柄页，切换句柄就可以了。
    原则：
        1. 在selenium自动化时，尽可能保持有，且最多仅有两个页面存在。
        2. 如果页面会自行关闭，就不需要额外执行close（特定业务）
        3. 如果自动关闭后，仍需要操作其他页面，则需要切换句柄。
'''

# 切换句柄
handles = driver.window_handles  # 获取当前所有的句柄
# driver.close()  # 关闭当前句柄页
driver.switch_to.window(handles[1])  # 切换到第二个句柄页
print(handles)

sleep(3)
# 操作第二个句柄页
# print(driver.title)
# driver.find_element('link text', 'QQ登录').click()
# handles = driver.window_handles
# print(handles)


'''
    iframe是一个窗体，内嵌页面，本身是一个独立的html页面存在。本质上是套娃。
    对于iframe内的元素如果要操作，是没有办法直接定位的。
    当你如果遇到死活定位不到的元素，就检查一下是不是一个iframe，如果是，则切换iframe后再操作
    iframe在切换进去之后，就只可以操作iframe中的内容，iframe以外的内容无法操作。如果要操作原窗体内容，需要重新返回默认窗体
'''
# 切换iframe：有id就直接传入id即可，没有id，就通过元素定位，传递元素进去
frame = driver.find_element('id', 'ptlogin_iframe')
driver.switch_to.frame(frame)
# 执行QQ快捷登录
driver.find_element('id', 'img_out_508419907').click()
sleep(2)
# 返回默认窗体。
# driver.switch_to.default_content()

handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[0])
print(driver.title)
