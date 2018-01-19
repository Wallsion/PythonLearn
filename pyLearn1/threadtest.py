import _thread
from time import sleep,ctime
def loop0():
    print('start loop0 at' , ctime(),end = '\n')
    sleep(4)
    print('stop loop0 at' , ctime(),end = '\n')
def loop1():
    print('start loop2 at' , ctime(),end = '\n')
    sleep(2)
    print('stop loop2 at' , ctime(),end = '\n')
def main():
    print('start', ctime())
    #loop0()
    #loop1()
    #print('stop' , ctime())
    _thread.start_new_thread(loop0,()) 
    _thread.start_new_thread(loop1,())
    sleep(6)
    print('all done',ctime())
if __name__ == "__main__":
    main()