import gevent
from gevent import monkey
import time

monkey.patch_all()


def coroutine_work(coroute_name):
    for i in range(10):
        print(coroute_name, i)
        time.sleep(0.5)


def main():
    gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2"),
    ])


if __name__ == '__main__':
    main()
