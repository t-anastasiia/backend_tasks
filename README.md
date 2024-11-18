<h1 align="center">FEFU backend tasks</h1>

<h2>Локальный запуск</h2>

<li>Клонируйте репозиторий</li>

```git clone git@github.com:t-anastasiia/backend_tasks.git```

<li>Перейдите в папку проекта</li>

```cd backend_tasks```

<li>Активируйте виртуальное окружение</li>

Для macOS и Linux:
```source myenv/bin/activate```

Для Windows:
```myenv\Scripts\activate```

<li>Установите зависимости</li>

```pip install -r requirements.txt```

<li>Примените миграции базы данных</li>

```python manage.py migrate```

</li>Запустите локальный сервер на порту 8001</li>

```python manage.py runserver 0.0.0.0:8000```

Проект теперь доступен по адресу:
http://{address}:8001/ ({address} - IP-адрес машины, где запущен сервер, чтобы узнать его, запустите на macOS и Linux: ```ifconfig | grep inet``` или на Windows: ```ipconfig```)

<h2 align="center">Task 1</h2>

Для запуска сервера не специфическом IP-адресе возможно прямым указанием его при запуске, например ```python manage.py runserver 192.168.1.10:8001```. Настройки, приложение и тд. в проекте присутствуют.

<h2 align="center">Task 2+Task3</h2>
Для выполнения GET и POST запросов через терминал можно использовать curl

```curl -X GET http://{address}:8000/{endpoint}/```
```curl -X POST http://{address}:8000/{endpoint}/ -H "Content-Type: application/json" -d '{"key": "value"}'```

где {endpoint} - имя эндпоинта

По <a href="https://disk.yandex.ru/d/AWNMfRUiP4T5_w">ссылке</a> также находятся коллекция и пространство переменных для работы через Postman. 

Эндпоинты для этого задания:
<ul>
  <li>http://{address}:8000/</li> server endpoint. ({address} заменить на свое значение)
  <li>get1/</li> первый get endpoint
  <li>get2</li> второй get endpoint
  <li>cat_info/</li> post+get endpoint. post запрос принимает form-data формат, а также json 
  
```
{
  "breed": "string",
  "rating": "string",
  "image_url": "string"
}
```
</ul>

<h2 align="center">Task 4+Task5</h2>
Методы авторизации и юзера осуществены в auth_views.py и user_views.py соотвественно. 
Эндпоинты для этого задания:
<ul>
  <li>http://{address}:8000/</li> server endpoint. ({address} заменить на свое значение)
  <li>register/</li> регистрация, осуществляется валидация всех полей, внутри create_user в user_views.py. принимает поля форматов form-data и json
  
  ```
  {
    "username": "string",
    "password": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string"
  }
  ```
  <li>login/</li> вход, принимает поля форматов form-data и json
  
  ```
  {
    "username": "string",
    "password": "string"
  }
  ```
  <li>get_user/{id}/</li> получении ифнормации о пользователе по id 
  <li>update_user/{id}/</li> обновлении информации о пользователе по id, не требует раннее пройденной авторизации
  <li>delete_user/{id}/</li> удаление пользователя по id

  create_user сделан недоступным напрямую, вызывается он лишь при регистрации. это не ошибка :) я так специально сделала
  
