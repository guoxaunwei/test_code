from time import sleep

from selenium import webdriver

# 启动浏览器:浏览器首字母要大写，还要添加()
driver = webdriver.Chrome()
# # 访问url:一定要在url中添加http://这样的内容,如果不加会报错，必须加//
# driver.get('http://www.baidu.com')
#
# driver.find_element('id','kw').send_keys('葫芦娃')
# driver.find_element('id','su').click()
# sleep(3)
# driver.quit()
driver.get('https://music.163.com/')
driver.maximize_window()
sleep(2)
driver.find_element('link text','登录').click()
sleep(3)
driver.find_element('link text','选择其他登录模式').click()
sleep(3)
driver.find_element('id','j-official-terms').click()
sleep(2)
driver.find_element('link text','QQ登录').click()
sleep(2)
# 获取所有句柄
all_handles=driver.window_handles

# 切换句柄
driver.switch_to.window(all_handles[1])
print(all_handles)
print(driver.title)
# 关闭当前句柄页
# driver.close()
sleep(3)
# 切换frame
frame=driver.find_element('id','ptlogin_iframe')
driver.switch_to.frame(frame)
driver.find_element('id','img_out_327731383').click()

sleep(3)

# 返回默认窗体。
# driver.switch_to.default_content()

driver.quit()