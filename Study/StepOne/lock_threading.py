import time
import threading


# 银行账户
balance = 0


def ChangeIt(num):
    # 先存后取结果为0
    global balance
    # 造成的原因是一个高级语言一句简单代码
    # 会在cpu中分解成多个命令执行
    # 然而线程调用是CPU交叉调用
    # 既是多个线程中的语句分解成很多命令然后这些命令被打乱执行
    # 这样就会出现数据混乱的结果
    balance += num
    balance -= num


# 加锁的线程
def RunLockThread(n):
    for i in range(1000000):
        #先获得锁
        threading.Lock().acquire()
        try:
            ChangeIt(i)
        finally:
            #释放锁
            threading.Lock().release()


def RunThread(n):
    # 只要这里循环次数偏多就会造成数据同时被修改的情况
    for i in range(10000000):
        ChangeIt(n)


t1 = threading.Thread(target=RunThread, args=(8,))
t2 = threading.Thread(target=RunThread, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
