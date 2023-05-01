from multiprocessing import Process
from threading import Thread


def demo1(N):
    flag = True
    for i in range(N):
        flag = not flag
    print('end')

def test1(N):
    print("Single thread")
    demo1(N)
    demo1(N)

def test2(N):
    print("Two thread with Python threading library")
    thread1 = Thread(target=demo1, args=(N,))
    thread2 = Thread(target=demo1, args=(N,))
    thread1.start()
    thread2.start()
    # thread1.join()
    # thread2.join()

def test3(N):
    print("Two process")
    p1 = Process(target=demo1, args=(N,))
    p2 = Process(target=demo1, args=(N,))
    # p3 = Process(target=demo1, args=(N,))
    # p4 = Process(target=demo1, args=(N,))
    # p5 = Process(target=demo1, args=(N,))
    # p6 = Process(target=demo1, args=(N,))
    p1.start()
    p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
 



if __name__ == '__main__':
    # test1(int(1e9))
    # test2(int(1e9))
    test3(int(1e9))