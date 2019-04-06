# Multiple django project with one url

Route multiple django project to one url with nginx and mini.

Static and media files will be served from minio server like cdn.

Rest is configuring base url prefix for each django project and configure nginx with same shape.

**django_1**

urls.py
```
urlpatterns = [
    path('v1/', index, name='index'),
    path('v1/about/', about, name='about'),
    path('v1/admin/', admin.site.urls),
]
```

**django_2**

urls.py
```
urlpatterns = [
    path('v2/', index, name='index'),
    path('v2/about/', about, name='about'),
    path('v2/admin/', admin.site.urls),
]
```

**django_3**

urls.py
```
urlpatterns = [
    path('v3/', index, name='index'),
    path('v3/about/', about, name='about'),
    path('v3/admin/', admin.site.urls),
]
```

**nginx configuration**

```
upstream django1 {
  ip_hash;
  server 192.168.1.33:8001;
}
upstream django2 {
  ip_hash;
  server 192.168.1.33:8002;
}
upstream django3 {
  ip_hash;
  server 192.168.1.33:8003;
}

server {
    # root /index.html

    location /v1/ {
        proxy_pass http://django1/v1/;
    }

    location /v2/ {
        proxy_pass http://django2/v2/;
    }

    location /v3/ {
        proxy_pass http://django3/v3/;
    }

    listen 80;
}
```

## Usage

1. Run minio storage
    ```
    cd minio
    docker-compose up -d --build
    ```

2. Run each django projects
    ```
    cd django{1,2,3}
    docker-compose up -d --build
    ```

3. Run home application
    ```
    cd home
    docker-compose up -d --build
    ```

4. Now check [http://localhost](http://localhost) and test it.