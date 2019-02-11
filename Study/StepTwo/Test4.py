
# 计算区间利润


def GetMoney(totalMoney):
    arr=[1000000,600000,400000,200000,100000,0]
    rat=[0.01,0.015,0.03,0.05,0.075,0.1]
    r=0
    for i in range(0,6):
        if totalMoney>arr[i]:
            r+=(totalMoney-arr[i])*rat[i]
            totalMoney=arr[i]
    return r
            
        
totalMoney=int(input('利润为：'))
profit=GetMoney(totalMoney)
print('利润为{0},奖金为{1}'.format(totalMoney,profit))