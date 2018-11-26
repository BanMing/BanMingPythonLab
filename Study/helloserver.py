#导入wsgiref模块
from wsgiref.simple_server import make_server
#导入我们自己写的application
from helloweb import application

#创建一个服务器，ip地址为空，端口8000，处理函数是application
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求：
httpd.serve_forever()