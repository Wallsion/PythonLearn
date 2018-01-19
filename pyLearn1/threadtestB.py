import _thread
from time import ctime,sleep
loops = [2,4]
def loop(nloop,nsec,lock):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('stop loop',nloop,"at",ctime())
    lock.release()
def main():
    print('starting at:',ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    print('all done at:',ctime())
if __name__ == "__main__":
    main()

