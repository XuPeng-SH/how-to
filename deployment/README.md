**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Nginx简单配置例子](#markdown-header-nginx%E7%AE%80%E5%8D%95%E9%85%8D%E7%BD%AE%E4%BE%8B%E5%AD%90)

## Nginx简单配置例子
MacOS下配置 `Nginx+UWSGI+Flask`
1. ```pip install uwsgi; brew install nginx```
2. 去到flask工程目录，创建wsgi.py:
    ```
    app = create_app()
    ```
3. 创建wsgi.ini [wsgi.ini.example](./wsgi.ini.example)
4. 运行: ```uwsgi --ini wsgi.ini```
5. MacOS下：
   ```cd /usr/local/etc/nginx;``` 加入如下配置到nginx.conf [nginx.conf.example](nginx.conf.example)
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
