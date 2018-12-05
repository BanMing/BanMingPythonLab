导航定位：

    element = driver.find_element_by_id("passwd-id")  #通过id获取元素

    element = driver.find_element_by_name("passwd")  #通过name获取元素

    element = driver.find_element_by_xpath("//input[@id='passwd-id']")  #通过使用xpath匹配获取元素

下拉框输入数据：

HTML文本：
    <select name="cars">
      <option value ="volvo">沃尔沃</option>
      <option value ="bmw">宝马</option>
      <option value="benz">奔驰</option>
      <option value="audi">奥迪</option>
    </select>
    
python操作：

    from selenium.webdriver.support.ui import Select  
    select = Select(driver.find_element_by_name('cars'))  #找到name为cars的select标签
    select.select_by_index(1)  #下拉框选中沃尔沃
    select.select_by_visible_text("宝马")  #下拉框选中宝马

    select.select_by_value("benz")  #下拉框选中奥迪

我们想要爬取的网站有些可能需要登录，这样就需要在请求网站的时候添加Cookies。

    driver.get("http://www.example.com") #先请求一个网页
    
    cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’} #设置cookie内容
    driver.add_cookie(cookie)  #添加cookie

![](https://inews.gtimg.com/newsapp_bt/0/6682637155/641)
