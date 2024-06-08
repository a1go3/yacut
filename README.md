# YaCut.
### Учебный проект Яндекс.Практикум. 
## Описание:
YaCut - это web-приложение и REST API для создания коротких URL-ссылок на различные web-страницы.
## Возможности приложения

- Генерация коротких ссылок и их связь с исходными длинными ссылками.
- Генерация случайной короткой ссылки в случае, если пользователь не указал свой вариант
- Переадресация на исходный адрес при обращении к коротким ссылкам.

## Работа с API:
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Используемые технологии
- Python 3.11
- Flask 3.0.2
- Jinja2 3.1.4
- SQLAlchemy 2.0.21

## Использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/tatarenkov-r-v/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
В корне проекта создайте файл переменных окружения `.env` со следующими переменными:
```
FLASK_APP=yacut
FLASK_ENV=<production или development>
DATABASE_URI=<dialect+driver://username:password@host:port/database>
SECRET_KEY=<секретный ключ>
```
Запуск проекта:

```commandline
flask run
```