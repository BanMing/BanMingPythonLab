from selenium import webdriver#导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys#导入keys

driver=webdriver.Chrome()#请求使用指定浏览器
driver.get("http://www.python.org")

assert "Python" in driver.title #看看Python关键字是否在网页title中，如果在则继续，如果不在，程序跳出。
elem=driver.find_element_by_name("q")#找到name为q的元素 这里是个搜索框
elem.clear()#清空搜索框内容
elem.send_keys("pycon")#在搜索框中输入pycon
elem.send_keys(Keys.ENTER)#模拟按下回车键
assert 'No result found.' not in driver.page_source #如果当前页面有“no results found.”则程序跳出
driver.close()#关闭webdriver

