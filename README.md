## EducaCMS  (проект находится в разработке)

# Платформа для онлайн - обучения с собственной системой управления содержимым.(CMS)
API для проекта "Библиотека онлайн фильмов"

##### _разработка Spiridonov R.A aka Speccy_

## Окружение проекта:
  * 
  * 
  * 
  * 

Склонируйте репозиторий с помощью git

   https://github.com/Speccy-Rom/EducaCMS.git
Перейти в папку:
```bash
cd EducaCMS
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/
