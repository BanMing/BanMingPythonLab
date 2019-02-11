import re
s = 'ABC\\-001'
print(s)
# 表示'ABC\-001'
# 可以使用r前缀来替换转移字符
s = r'ABC\-001'
print(s)

test = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(test.string)
# test.string

