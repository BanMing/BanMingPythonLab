import requests

# r=requests.get('https://www.dous

# print(r.text)

#传入参数
# r=requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
# print(r.url)
# #默认编码utf8
# print(r.encoding)

# print(r.content)

#post默认content-type为application/x-www-form-urlencoded
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)

#上传文件
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url='', files=upload_files)