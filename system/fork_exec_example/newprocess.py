import os

def child():
    print(f'Hello from child {os.getpid()}')
    os._exit(0)

child()
