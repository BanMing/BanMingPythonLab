import requests
keyDict = {'key1': 'value1', 'key2': 'value2'}
req = requests.get('http://httpbin.org/get', params=keyDict)
print('URL已经正确编码：', req.url)
print('字符串方式的响应体：\n', req.text)
