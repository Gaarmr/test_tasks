1. Клонировать этот репозиторий 
```sh
git clone http://
```

2. Создать файл .env в корне проекта и описать переменные 
```ini
POSTGRES_USER = i-sberg
POSTGRES_PASSWORD = i-sberg
POSTGRES_DB = i-sberg
```

3. Выполнить команду 
```sh
docker run -d --name test-redis -p 6379:6379 redis
docker-compose up -d
``