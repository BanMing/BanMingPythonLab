
import re
content = '你好$$$我正在学Python@#@现在需要&*&*&修改字符串'
print(content.replace('$$$', ' ').replace('@#@', ' ').replace('&*&*&', ' '))
# 正则表达式
print(re.sub('[$@*#&%]+', ' ', content))