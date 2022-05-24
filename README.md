# Instruction 


| Key | Value                       |
| ------- |-----------------------------|
| SECRET_KEY | Secret key for Django       |
| DEBUG | 1(True) or 0(False)         |
| SQL_ENGINE | The postgresql module       |
| SQL_DATABASE | Name of your database       |
| SQL_USER | Username of database user   |
| SQL_PASSWORD | Password from database      |
| SQL_HOST | Host DB in docker-compose   |
| SQL_PORT | Usually 5432                |
| EMAIL_HOST_USER| Your email adress           |
| EMAIL_HOST_PASSWORD| Your email account password |

## Commands:

```
docker-compose up -d --build
```

```
docker-compose exec web python manage.py migrate
```

```
docker-compose exec web python manage.py createsuperuser
```
To stop container:

```
docker-compose down
```

To run container again

```
docker-compose up 
```
