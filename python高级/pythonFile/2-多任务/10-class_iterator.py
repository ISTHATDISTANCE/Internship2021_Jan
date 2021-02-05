import time


class Classmate(object):
    def __init__(self):
        self.name = list()
        self.current_idx = 0

    def add(self, str):
        self.name.append(str)

    # 一个类有__iter__方法则被认为是可迭代的；如果还有__next__方法则被成为迭代器
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < len(self.name):
            ret = self.name[self.current_idx]
            self.current_idx += 1
            return ret
        else:
            # 抛出系统异常，停止迭代
            raise StopIteration


classmate = Classmate()
classmate.add("ltt")
classmate.add("mkk")
classmate.add("hss")
for i in classmate:
    print(i)
    time.sleep(1)
