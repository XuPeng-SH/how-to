## 如何使用LLDB调试进程的子进程
1. ```lldb -- myApp arg1 arg2```
2. 在```fork```前设置breakpoint
3. 打开新的Terminal,使用lldb等待调试进程产生的新的子进程
```js
lldb process attach -n myApp -w
```
4. 父进程lldb继续运行，触发子进程，子进程将会在新开的Terminal里进入调试模式

## 如何获取库相关路径
```js
echo | clang -v -E -x c++ -
```

## c中如何实现亚秒精度睡眠
```js
#include <sys/select.h>
timeout->sec = 1;
timeout->usec = 20303;
select(0, NULL, NULL, timeout);
```
