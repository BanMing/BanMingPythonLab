from multiprocessing import Process
import os

#子进程要执行

def run_proc(name):
    print('run child process %s (%s)...' %(name,os.getpid()))

if __name__=='__main__':
    print('parent process %s.' % os.getpid())
    p=Process(target=run_proc, args=('test',))
    # p=Process(traget=run_proc,args=('banming',))
    print('Child will start')
    p.start()
    #等待子进程结束后再继续往下运行
    p.join()
    print('Child process will end')
