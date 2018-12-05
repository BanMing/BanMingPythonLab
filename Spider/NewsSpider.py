import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os

# newsTypes=['auto','edu','house']
newsTypes=['sports','news','ent','finance','tech','games','auto','edu','house']

def main():
    for news in newsTypes:
        # print(news)
        GetNews(news)
    print('Get Down')
    # GetNews('http://games.qq.com/articleList/rolls/')



def GetNews(news):

    url='http://'+news+'.qq.com/articleList/rolls/'
    #设置手机浏览器访问
    options=webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
    
    driver=webdriver.Chrome(chrome_options=options)
    
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'lxml')

    # 先找到父节点
    titMode=soup.find_all('ul','titMode')
    #根据父节点获取子节点

    if titMode== None or titMode.__len__()==0:
        return
    lilist = titMode[0].find_all_next('li')    
    f=open('Spider/News/'+news+'TodayNews.md','w')

    #遍历所有子节点获取内容
    for li in lilist:
        #判断是否是空
        if li.find('strong')==None:
            # print(li)
            break
        
        #标题
        content=li.find('strong').text+li.find('span').text
        # print(content)
        f.write(content+'\n\n')
        #图片
        a=li.find('a',target='_blank')
        itemUrl=a['href']
        driver.get(itemUrl)
        soupItem=BeautifulSoup(driver.page_source,'lxml')
        img=soupItem.find('img')
        if img!=None and img.has_key('src'):
            # print(img['src'])
            f.write('![](https:'+img['src']+')'+'\n\n')
        # print(soupItem.find('img'))
        # print(soupItem.find('img')['src'])
        
        

    f.close()
    driver.quit()
        


main()
