from python_class import lesson_01  #导入封装函数文件
from test_data import test_date
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
# 调用函数  1.先参数取出来，  2，再传参到函数调用里
url= test_date.url['url']  #取值url
user= test_date.login_date['username']   #取值登录用户名
pwd= test_date.login_date['password']   #取值登录密码
s_key= test_date.searchNumber['searchNumber']     #取值订单号
print(url,user,pwd,s_key)
#函数调用
#给函数定义一个返回值
result=lesson_01.search_key(driver=driver,url=url,username=user, password=pwd, searchNumber=s_key)
print(result)
if s_key in result:
    print('订单搜索结果是正确的！')
else:
    print('订单搜索结果错误！')