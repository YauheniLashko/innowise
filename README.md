# innowise test

## Instruction 


| Key | Value                       |
| ------- |-----------------------------|
| SECRET_KEY | Secret key for Django       |
| POSTGRES_NAME | Name of your database       |
| POSTGRES_USER | Username of database user   |
| POSTGRES_PASSWORD | Password from database      |
| EMAIL_HOST_USER| Your email adress           |
| EMAIL_HOST_PASSWORD| Your email account password |

Commands:

```
docker-compose up -d --build
```

```
docker-compose exec web python manage.py makemigrations
```

```
docker-compose exec web pythoon manage.py migrate
```
To stop container:

```
docker-compose down
```

To run container again

```
docker-compose up 
```
