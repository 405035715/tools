import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        print(threading.get_ident())
        print(threading.main_thread())
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    # t1 = threading.Thread(target=loop, name='loopThread1')
    t.start()
    # t1.start()
    print(threading.active_count())
    print(threading.enumerate())
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
