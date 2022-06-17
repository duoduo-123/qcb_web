import time

def login_page(username, password, driver):  # 形参  参数化，提高代码复用率
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('btnSubmit').click()
def open_url(url, driver):  # 打开网页
    driver.get(url)
    driver.maximize_window()
def search_key(url, driver, username, password, searchNumber):
    open_url(url, driver)
    login_page(username, password, driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    p_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    F_id = p_id + '-frame'
    driver.switch_to.frame(F_id)
    driver.find_element_by_id('searchNumber').send_keys(searchNumber)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    # num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    # if searchNumber in num:
    #     print('订单搜索结果是正确的！')
    # else:
    #     print('订单搜索结果错误！')

