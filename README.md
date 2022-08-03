
```shell
 docker-compose up -d --build
```


```shell
docker-compose exec web python manage.py migrate --noinput

```


```shell
docker-compose exec web python manage.py createsuperuser 

```