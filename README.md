# DRF
### Установка и запуск

1. Активируйте виртуальное окружение:
```bash
poetry shell
```

2. Установите зависимости:
```bash
poetry install
```

3. Создайте файл .env в корневой директории проекта:
```env
SECRET_KEY=your-secret-key
POSTGRES_DB=your-db-name
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

### Запуск с Docker
```bash
docker-compose up --build
```
## Поддержка
