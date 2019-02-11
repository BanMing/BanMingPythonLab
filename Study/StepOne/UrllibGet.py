from urllib import request
import ssl
#使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
#修复bug：python  certificate verify failed: unable to get local issuer certificate
context=ssl._create_unverified_context()
with request.urlopen('https://api.douban.com/v2/book/2129650',context=context) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))