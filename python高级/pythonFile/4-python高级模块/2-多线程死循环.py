import threading

def test():
    while True:
        pass
    
t = threading.Thread(target=test)
t.start()

while True:
    pass