
from selenium import webdriver#导入Selenium的webdriver
import time

def scroll_down(self,driver,times):
    for item in range(times):
        print('开始执行第',str(item+1),'下拉操作')
        #执行下拉操作的js命令
        driver.execute_script('window.scrollTo(0,docment.body.scrollHeight);')
        print('第',str(item+1),'次下拉操作执行完毕')
        print('第',str(item+1),'次等待网页加载。。。。')
        time.sleep(20)#等待20秒
