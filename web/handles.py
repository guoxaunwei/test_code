from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('http:\\www.baidu.com')
# 隐式等待
driver.implicitly_wait(10)
# 窗口最大化
driver.maximize_window()
driver.find_element('xpath','//input[@id="kw"]').send_keys('葫芦娃')
driver.find_element('xpath','//input[@id="su"]').click()
sleep(5)
driver.find_element('xpath','//*[@id="2"]/h3/a').click()
sleep(3)
el=driver.window_handles
print(el)
driver.switch_to.window(el[1])
driver.close()

driver.switch_to.window(el[0])

driver.find_element('link text','登录').click()
print('*'*20)


driver.find_element('xpath','//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()
# 进入frame之前要切换句柄
handles=driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
# 进入iframe
frame = driver.find_element('id','ptlogin_iframe')
driver.maximize_window()
driver.switch_to.frame(frame)
# 登录
driver.find_element('id','img_out_327731383').click()
sleep(3)

handles=driver.window_handles
print(handles)
# 打印当前页面title
print(driver.title)
handles1=driver.window_handles
driver.switch_to.window(handles1[0])

text=driver.find_element('xpath','//span[text()="二手锅子"]').text
print(text,'打印文本')
if driver.find_element('xpath','//span[text()="二手锅子"]').text=='二手锅子':
    print('断言成功')
else:
    print('断言失败')

assert driver.find_element('xpath','//span[text()="二手锅子"]').text =='二手锅子' ,'断言失败'

# 鼠标悬停操作
element=driver.find_element('xpath','//span[text()="二手锅子"]')
ActionChains=ActionChains(driver)
ActionChains.move_to_element(element).perform()
sleep(3)
# 退出登录
driver.find_element('link text','退出').click()
assert driver.find_element('link text','登录').text == '登录','断言失败'
print('------------------')

text1 = driver.find_element('link text', '登录').text
if text1=='登录1':
    print('断言成功')
else:
    print('断言失败')
    try:
        save = driver.save_screenshot('D:\\测试截图\\bug.png')
        print('%s：截图成功' % (save))
    except BaseException as e:
        print(f'{e}:截图失败')


sleep(5)
driver.quit()