from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    print("The file is opened successfully")
    # yield后的内容在出现异常或者执行完毕后执行，这保证了文件一定会被关闭
    yield f
    f.close()
    print("The file is closed successfully")


with my_open('out.txt', 'w') as f:
    f.write("This is the simplest context manager")
