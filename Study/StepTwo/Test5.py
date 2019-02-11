import  operator
#排序
numDict={1:2,3:4,2:1,0:0}
sortNumDict=sorted(numDict.items(),key=operator.itemgetter(1))
print(sortNumDict)