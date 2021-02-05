import threading
import time


def test1(temp):
    temp.append(33)
    print(temp)


def test2(temp):
    print(temp)


nums = [11, 22]


def main():
    t1 = threading.Thread(target=test1, args=(nums,))
    t2 = threading.Thread(target=test2, args=(nums,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
