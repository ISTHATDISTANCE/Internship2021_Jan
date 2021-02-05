import threading
import time

num = 0

def test1(temp):
    global num
    # 如果没有上锁则上锁；如果上锁了则等着
    print("1:")
    for i in range(temp):
        mutex.acquire()
        num += 1
        mutex.release()
    print(num)


def test2(temp):
    global num
    print("2:")
    for i in range(temp):
        mutex.acquire()
        num += 1
        mutex.release()
    print(num)

mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(1)
    print(num)

if __name__ == '__main__':
    main()
