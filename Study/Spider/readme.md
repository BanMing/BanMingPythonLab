http://httpbin.org/get
http请求工具

use-agent:
https://zh.wikipedia.org/wiki/%E7%94%A8%E6%88%B7%E4%BB%A3%E7%90%86

因此，为获取更好的网页，绝大多数网页浏览器使用的User-Agent值如下：

    Mozilla/[version] ([system and browser information]) [platform] ([platform details]) [extensions]。

iPad上的Safari使用的就是下述：

    Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405

|字符串|说明|
|:-----:|:---:|
|Mozilla/5.0	Mozilla/5.0 |是一个通用标记符号，用来表示与 Mozilla 兼容，这几乎是现代浏览器的标配。|
|（iPad; U; CPU OS 3_2_1 like Mac OS X; en-us）|	浏览器所运行的系统的详细信息|
|AppleWebKit/531.21.10|浏览器所使用的平台|
|（KHTML, like Gecko）|浏览器平台的细节|
|Mobile/7B405|被浏览器用于指示特定的直接由浏览器提供或者通过第三方提供的可用的增强功能。这方面的一个实例是Microsoft Live Meeting，它注册了一个扩展以使Live Meeting服务知道该软件是否已经安装上，这意味着它可以为加入会议提供一个简化的体验。|

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

火狐电脑端：

    Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
    Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0

谷歌：
    
    Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36


list of use-agent:
https://deviceatlas.com/blog/list-of-user-agent-strings



BeautifulSoup找到的对象可以直接用【.】出来他的子对象，如果有多个就是直接返回第一个

Selenium选择元素的方式：
find_element_by_css_selector:通过元素的class选择，如<div class='bdy-inner'>test</div>可以使用