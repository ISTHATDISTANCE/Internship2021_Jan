import multiprocessing

def test():
    while True:
        pass
    
t = multiprocessing.Process(target=test)
t.start()

while True:
    pass