<h1 align="center">FEFU backend tasks</h1>

<h2>Требования</h2>
<p>- Python 3.12</p>
<p>- Django 3.2 или выше</p>

<h2>Деплой на удалённый сервер</h2>

Проект развернут на платформе Render и доступен по адресу:
```https://backend-tasks-9r0i.onrender.com```

Запросы к API выполняются по этому серверу с использованием указанных ниже эндпоинтов.

<h2 align="center">Task 1</h2>

Для запуска сервера не специфическом IP-адресе возможно прямым указанием его при запуске, например ```python manage.py runserver 192.168.1.10:8001```. Настройки, приложение и тд. в проекте присутствуют.

<h2 align="center">Task 2+Task3</h2>
Для выполнения GET и POST запросов через терминал можно использовать curl

```bash
curl -X GET https://backend-tasks-9r0i.onrender.com/{endpoint}/
curl -X POST https://backend-tasks-9r0i.onrender.com/{endpoint}/ -H "Content-Type: application/json" -d '{"key": "value"}
```
где {endpoint} - имя эндпоинта.

По <a href="https://disk.yandex.ru/d/AWNMfRUiP4T5_w">ссылке</a> также находятся коллекция и пространство переменных для работы через Postman. 

Эндпоинты для этого задания:
<ul>
  <li>https://backend-tasks-9r0i.onrender.com/</li> server endpoint
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
  <li>https://backend-tasks-9r0i.onrender.com/</li> server endpoint
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
  
