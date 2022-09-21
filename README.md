
```shell
 docker-compose up -d --build
```


```shell
docker-compose exec web python manage.py migrate --noinput

```


```shell
docker-compose exec web python manage.py createsuperuser 

```


###CREATE CARS

```shell
docker-compose exec web python manage.py create_cars

```


###CREATE CUSTOMERS
```shell
docker-compose exec web python manage.py create_customers

```

###CREATE SHOWROOMS
```shell
docker-compose exec web python manage.py create_showrooms

```

###CREATE DEALERS
```shell
docker-compose exec web python manage.py create_dealers

```