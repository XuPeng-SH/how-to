<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Nginx简单配置例子](#nginx%E7%AE%80%E5%8D%95%E9%85%8D%E7%BD%AE%E4%BE%8B%E5%AD%90)
- [如何在已有镜像上加装环境生成新的镜像](#%E5%A6%82%E4%BD%95%E5%9C%A8%E5%B7%B2%E6%9C%89%E9%95%9C%E5%83%8F%E4%B8%8A%E5%8A%A0%E8%A3%85%E7%8E%AF%E5%A2%83%E7%94%9F%E6%88%90%E6%96%B0%E7%9A%84%E9%95%9C%E5%83%8F)
- [如何ssh到容器](#%E5%A6%82%E4%BD%95ssh%E5%88%B0%E5%AE%B9%E5%99%A8)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Nginx简单配置例子](#markdown-header-nginx%E7%AE%80%E5%8D%95%E9%85%8D%E7%BD%AE%E4%BE%8B%E5%AD%90)

## Nginx简单配置例子
MacOS下配置 `Nginx+UWSGI+Flask`
1. ```pip install uwsgi; brew install nginx```
2. 去到flask工程目录，创建wsgi.py:
    ```
    app = create_app()
    ```
3. 创建wsgi.ini [wsgi.ini.example](./nginx_simple_example/wsgi.ini)
4. 运行: ```uwsgi --ini wsgi.ini```
5. MacOS下：
   ```cd /usr/local/etc/nginx;``` 加入如下配置到nginx.conf [nginx.conf.example](./nginx_simple_example/nginx.conf)
   ```js
   server {
        listen 80;
        server_name s1.auth;

        location / {
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8000;
        }
   }
   ```
   运行：```nginx -c /usr/local/etc/nginx/nginx.conf```

## 如何在已有镜像上加装环境生成新的镜像
CentOS加装ssh服务举例
1. ```docker pull centos:6.6```
2. ```js
docker run -it centos:6.6 bash
yum install ssh
exit
```
3. ```docker ps -a``` 找出container ID, ```docker commit $containerID centos-ssh```生成新的centos-ssh镜像

## 如何ssh到容器
主机ssh本地容器示例
1. ```docker run -d -p 8888:22 centos-ssh sshd -D```
2. 本地终端输入：```ssh root@127.0.0.1 -p 8888```
