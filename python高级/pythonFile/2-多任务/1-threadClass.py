import threading
import time


class myThread(threading.Thread):
    def run(self) -> None:
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)
        self.lo()

    def lo(self):
        for i in range(4):
            time.sleep(1)
            msg = "You're " + self.name + " @ " + str(i)
            print(msg)


if __name__ == '__main__':
    t = myThread()
    t.run()
