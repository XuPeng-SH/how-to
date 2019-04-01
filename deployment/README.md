## Nginx简单配置例子
MacOS下配置 `Nginx+UWSGI+Flask`
1. ```pip install uwsgi; brew install nginx```
2. 去到flask工程目录，创建wsgi.py:
    ```
    app = create_app()
    ```
3. 创建wsgi.ini [wsgi.ini.example](./nginx_simple_example/wsgi.ini)
4. 运行: ```uwsgi --ini wsgi.ini```
5. Ubuntu下：
   ```sudo ln -s myngix.conf /etc/nginx/sites-enabled/``` 加入如下配置到nginx.conf [mynginx.conf.example](./nginx_simple_example/mynginx.conf)
   ```js
   upstream my-servers {
        server 127.0.0.1:8000;
   }

   server {
        listen 80;
        server_name localhost;

        location / {
            include uwsgi_params;
            proxy_pass http://my-servers;
        }
   }
   ```
   运行：```nginx -c /usr/local/etc/nginx/nginx.conf```
   或运行Ubuntu：```sudo systemctl restart nginx```
   删除nginx default：```sudo rm /etc/nginx/sites-enabled/default```

## 如何在已有镜像上加装环境生成新的镜像
CentOS加装ssh服务举例
1. ```docker pull centos:6.6```
2. 步骤
   ```js
   docker run -it centos:6.6 bash
   yum install ssh
   exit
   ```
3. ```docker ps -a``` 找出container ID, ```docker commit $containerID centos-ssh```生成新的centos-ssh镜像

## 如何ssh到容器
主机ssh本地容器示例
1. ```docker run -d -p 8888:22 centos-ssh sshd -D```
2. 本地终端输入：```ssh root@127.0.0.1 -p 8888```

## uWSGI部署keras服务
1. lazy-apps = true # keras服务可能会阻塞

## 怎么生成Self-Signed证书
```
openssl req \
       -newkey rsa:2048 -nodes -keyout registry.key \
       -x509 -days 365 -out registry.crt
```
