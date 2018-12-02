import os

print(f'current pid={os.getpid()}')
pid = os.fork()
if pid == 0:
    print(f'child getpid={os.getpid()} pid={pid}')
    # os.execlp('python', 'python', 'newprocess.py')
    os.execvp('python', ('python', 'newprocess.py'))
    assert False, 'for child error'
else:
    print(f'parent getpid={os.getpid()} pid={pid}')
