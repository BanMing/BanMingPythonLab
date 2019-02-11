a = 1

# 数值是值类型
def fun(a):
    a = 2


fun(a)

print(a)

a = []

#list是引用类型
def fun1(a):
    a.append(1)


fun1(a)

print(a)
