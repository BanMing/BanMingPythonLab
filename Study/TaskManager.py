import time
import random
import queue
from multiprocessing.managers import BaseManager

# 发送任务队列
taskQueue = queue.Queue()
# 接收结果队列
resultQueue = queue.Queue()

class QueueManager (BaseManager):
    pass

#把两个队列注册到网络上，使用callable关联在一起
QueueManager.register('taskQueue',callable=lambda : taskQueue)
QueueManager.register('resultQueue',callable=lambda :resultQueue)

#绑定端口5000，设置验证码‘abc’:
manager=QueueManager(address=('',5000),authkey=b'abc')

#启动队列
manager.start()

#通过网络访问queue对象
task=manager.get_taskQueue()
result=manager.get_resultQueue()

#放几个任务进去
for i in range (10):
    n=random.randint(0,10000)
    print('Put task %d..' % n)
    task.put(n)

#从result中读取
print('Try get result...')
for i in range(10):
    r=result.get(timeOut=10)
    print('Result is %s' % r)

#关闭
manager.shutdown()
print('master exit')

