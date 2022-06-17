'''
import selenium  把工具里的所有内容都导入--一般不用
from...import  从哪里导入什么
from selenium import webdriver ：从selenium中导入webdriver库
import time  导入time这个模块---python自带的，不需要下载
selenium:python的工具，三个部分
ide：录制脚本--用的少
webdriver:库：提供对网页的各种操作+结合语言使用--python/java
3）grid：分布式---用的少
'''
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver=webdriver.Chrome()  #选择chrome这个浏览器，初始化driver===可以与浏览器进行沟通，建立会话：session
# # 1.打开一个网址
# driver.get('http://erp.lemfix.com/login.html')
# # # 2.浏览器窗口最大化
# driver.maximize_window()
# # 3.打开新页面
# time.sleep(3)  #等待三秒，默认单位秒
# driver.get('https://www.douyu.com/directory/myFollow')
# #4。向前、退后 刷新
# driver.back()  #返回上一个页面
# driver.forward()  #前进到下一个页面
# driver.refresh()  #刷新页面
# #5.退出
# driver.quit()  #关闭驱动  session关闭
# driver.close   #关闭当前窗口，不会关闭驱动
'''
浏览器常规操作，非常规操作需要用元素定位来实现
八大元素定位方法：
1）id：类比身份账号===仅限于当前页面
   注意：如果id不是固定的话，就不能用它定位
2）xpath
   1.绝对路径：如柠檬ERP标题：/html/body/div/div/div[1]/a/b---根节点，顺序性，继承关系
    ===面试不说，工作不用
    相对路径：标签名+属性=//标签名[@属性名=属性值]
           如：//input[@id='username']   ---xpath表达方式
   2.层级定位：只靠自己的特征定位：//标签名[@属性名=属性值]//标签名[@属性名=属性值]
    如柠檬ERP://div[@class='login-logo']//b
   3.文本属性定位： //b[text()='柠檬班ERP'] 
   4.包含属性值：//标签名[contains(@属性名/text(),属性值)]
     如：//input[contains(@class,'username')]
3）name

页面等待：
   1）强制等待：time.sleep()
   2)智能等待：隐形等待：driver.implicitly_wait()
   
找到元素后的操作
1.点击:click
2.输入内容:send_keys
3.获取文本：text
4.获取属性：get_athribute

'''

'''
1.识别是否有子页面的方式：页面层级路径里出现iframe：需要去切换iframe，才可以进行元素定位
'''
#打开页面
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://erp.lemfix.com/login')
driver.maximize_window()
driver.implicitly_wait(10)
#验证页面标题
page_text =driver.find_element_by_xpath("//div[@class='login-logo']//b").text  #找到元素位置，获取文本
print(page_text)

# 正常登录
driver.find_element_by_id('username').send_keys('test123')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnSubmit').click()
driver.implicitly_wait(10)
#用户名是否为测试用户
yonghu_text=driver.find_element_by_xpath("//p[text()='测试用户']").text
print(yonghu_text)

#点击菜单能正常打开
driver.find_element_by_xpath('//span[text()="零售管理"]')
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
# driver.find_element(by=By.XPATH, value='//span[text()="零售管理"]').click()

#查询314订单
# driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys(314)  #找不到，因为他有iframe标签
#1.通过找到这个元素--获取id属性
p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
F_id=p_id+'-frame'
# 通过id进行iframe的转换
driver.switch_to.frame(F_id)
driver.find_element_by_id('searchNumber').send_keys('955')
# 2.通过元素定位（xpath）来切换iframe====扩展
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id={}]'.format(F_id)))
# driver.find_element_by_id('searchNumber').send_keys('955')

# 3.通过iframe下标进行定位:下标值以html为基准，0开始
# driver.switch_to.frame(1)
# driver.find_element_by_id('searchNumber').send_keys('955')

# 点击查询
driver.find_element_by_id("searchBtn").click()
time.sleep(1)
#确定订单正确性
num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if '955' in num :
    print('订单搜索结果是正确的！')
else:
    print('订单搜索结果错误！')


'''
web自动化测试
工作中主要用于冒烟测试
工作中常与定义函数结合使用
分为执行文件，数据文本
'''


