from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_name('input')