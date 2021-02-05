# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import threading


def sing():
    for i in range(5):
        print(i)
        time.sleep(1)


def dance():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_hi(name):
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        li = threading.enumerate()
        length = len(li)
        print(li, length)
        if length <= 1:
            break
        time.sleep(0.5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
