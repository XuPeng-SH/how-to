<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Fork与exec家族](#fork%E4%B8%8Eexec%E5%AE%B6%E6%97%8F)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## fork与exec家族 [fork_exec_example](./fork_exec_example)
### fork
1. ```fork()```调用后会创建一个新的子进程,这个子进程是原父进程的副本.子进程可以独立父进程外运行.
2. ```fork()```是一个很特殊的方法,一次调用,两次返回
3. ```fork()```它会返回2个值,一个值为0,表示在子进程返回;另外一个值为非0,表示在父进程中返回子进程ID

```js
import os

def child():
    print(f'child process {os.getpid}')
    os._exit(0)

pid = os.fork()
if pid == 0:
    print(f'pid={pid} getpid={os.getpid()}')
    child()
else:
    print(f'pid={pid} getpid={os.getpid()}')
```
运行结果如下
```js
pid=0 getpid=29888
pid=29887 getpid=29887
child process 29888
```
