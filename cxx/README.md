<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [如何使用LLDB调试进程的子进程](#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8lldb%E8%B0%83%E8%AF%95%E8%BF%9B%E7%A8%8B%E7%9A%84%E5%AD%90%E8%BF%9B%E7%A8%8B)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 如何使用LLDB调试进程的子进程
1. ```lldb -- myApp arg1 arg2```
2. 在```fork```前设置breakpoint
3. 打开新的Terminal,使用lldb等待调试进程产生的新的子进程
```js
lldb process attach -n myApp -w
```
4. 父进程lldb继续运行，触发子进程，子进程将会在新开的Terminal里进入调试模式
