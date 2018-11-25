from multiprocessing import Pool
import os,time,random

def run_time_process(name):
    print('Run task %s (%s)'% (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('%s start run %0.2f end %0.2f' %(name,start,end))

if __name__=='__main__':
    print('parent process is %s.' % os.getpid())  
    pool=Pool(4)
    for i in range(5):
        pool.apply_async(run_time_process,args=(i,))
        # pool.apply_async(run_time_process, args=(i,))
    print('Wait for all process done...')
    pool.close()
    pool.join()
    print('All process done')