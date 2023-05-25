# SkyPro <img src="https://github.com/cestxvcdim/skypro_static/blob/main/icons/skypro_logo.png" width="35">

## Exam at the end of second semester

---

### About project:

- It's simple application on `Flask` with based `API` *(CRUD)*
- Applications runs from `Docker` container <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" width="25">
- Realize `CI/CD` logic and deploy at server with `GitHub Actions`

---

### Requirements:

```python
aniso8601==9.0.1
attrs==23.1.0
click==8.1.3
Flask==2.3.2
flask-restx==1.1.0
Flask-SQLAlchemy==3.0.3
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.17.3
MarkupSafe==2.1.2
marshmallow==3.19.0
packaging==23.1
PyJWT==2.7.0
pyrsistent==0.19.3
pytz==2023.3
SQLAlchemy==2.0.15
typing_extensions==4.6.1
Werkzeug==2.3.4
pytest==7.3.1
```

---

### How to use:

1) Copy [this adress](http://127.0.0.1:5000) in a browse page
2) Write a **GET/POST/PUT/DELETE** request in the page
3) Receive a response in `JSON` format from the site

---

### Examples:

#### Request: GET http://127.0.0.1:5000/notes

#### Response:

```json
[
    {
        "id": 1, 
        "name": "Note 1", 
        "text": "Hello world!"
    }, 
    {
        "id": 2, 
        "name": "Note 2", 
        "text": "Code your way to success"
    }, 
    {
        "id": 3, 
        "name": "Note 3", 
        "text": "Test"
    }
]
```

#### Request: GET http://127.0.0.1:5000/notes/2

#### Response:

```json
{
    "id": 2, 
    "name": "Note 2", 
    "text": "Code your way to success"
}
```

#### Request: POST http://127.0.0.1:5000/notes

```json
{
    "name": "Note 4", 
    "text": "New note"
}
```

#### Response:

```json
{
    "id": 4
    "name": "Note 4", 
    "text": "New note"
}
```

#### Request: PUT http://127.0.0.1:5000/notes/3

```json
{
    "name": "Updated note", 
    "text": "Updated text"
}
```

#### Response: 

```json
{
    "id": 3
    "name": "Updated note", 
    "text": "Updated text"
}
```

#### Request: DELETE http://127.0.0.1:5000/notes/2

#### Response:

```json
{
    "status": 200
}
```
---

## Virtual machine supported by _Yandex Cloud_<img src="https://github.com/cestxvcdim/skypro_static/blob/main/icons/yandex_logo.png" width="45">
