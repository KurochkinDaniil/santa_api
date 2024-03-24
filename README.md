# Тайный Санта

Проект "Тайный Санта" представляет собой RESTful API, разработанный с использованием FastAPI и PostgreSQL для организации игры "Тайный Санта".

## Начало работы

Для запуска проекта убедитесь, что на вашем компьютере установлены Docker и docker-compose.

### Конфигурация

1. Склонируйте репозиторий на ваш локальный компьютер:

   ```bash
   git clone <URL-адрес-репозитория>
   cd путь_к_проекту
    ```
2. Создайте файл .env в корне проекта со следующим содержанием:
    ```
    FAST_API_APP_HOST=0.0.0.0
    FAST_API_APP_PORT=8005
    DB_ENGINE=postgresql
    DB_PORT=5432
    DB_HOST=db
    DB_PASSWORD=postgres
    DB_NAME=auth
    DB_USER=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=auth
    ```
Измените значения переменных окружения в файле .env по вашему усмотрению.

### Запуск
1. Соберите и запустите контейнеры с помощью docker-compose:
    ```
    docker-compose up --build
    ```
    Эта команда соберет образ вашего приложения и запустит контейнеры для приложения и базы данных PostgreSQL.

2. После запуска контейнеров приложение будет доступно по адресу http://localhost:8005 (или другому порту, указанному в переменной FAST_API_APP_PORT в файле .env).

### Использование
Используйте следующие эндпоинты для взаимодействия с API:

- POST /group/: Создание новой группы.
- GET /groups/: Получение списка всех групп.
- GET /group/{group_id}: Получение информации о конкретной группе.
- PUT /group/{group_id}: Обновление информации о группе.
- DELETE /group/{group_id}: Удаление группы.
- POST /group/{group_id}/participant: Добавление участника в группу.
- POST /group/{group_id}/toss: Проведение жеребьевки и назначение подопечных участникам.
- GET /group/{group_id}/participant/{participant_id}/recipient: Получение информации о подопечном конкретного участника.

### Остановка
Для остановки и удаления контейнеров, созданных с помощью docker-compose, используйте следующую команду:
    ```
    docker-compose down
    ```
