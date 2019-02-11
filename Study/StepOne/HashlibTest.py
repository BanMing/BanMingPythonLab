import hashlib

md5 = hashlib.md5()

md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python haslib?'.encode('utf-8'))
print(md5.hexdigest())

# import hmac,random
