<!---![Workflow badge](https://github.com/theramblingrover/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)-->
# Учебный проект "REST API YaMDb".
## Яндекс.Практикум

### Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр (Genre) из списка предустановленных. Новые жанры может создавать только администратор. Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.


### Технологии проекта
- Python 3.9
- Django
- Django REST Framework
- PostgreSQL
- Simple-JWT
- Git
- Nginx
- Gunicorn
- Docker

### Запуск
- Клонировать репозиторий
```
git clone git@github.com:theramblingrover/yamdb_final.git
```
- Перейти в корневую папку проекта:
```
cd yambd_final
```
В файл ./infra/.env Поместить переменные настройки СУБД. Пример:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
- Выполнить запуск контейнеров:
```
make start
```
- Убедившись что контейнеры запущены, выполнить настройку приложения:
```
make configure
```
Для знакомства с проектом в репозитории имеется пример данных, которые могут быть загружены в БД командой:
```
make loadfixtures
```

### Остановка
- Для остановки выполнить в корневой папке проекта:
```
make stop
```

Подробная документация по API доступна по адресу http://localhost/redoc/.

### Участники проекта:
- Dmitriy839
- IamAlexandr
- theramblingrover
