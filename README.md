# 📝 To-Do List API - Django REST Framework

This is a simple **To-Do List API** project built with **Python** and **Django REST Framework**. It allows users to perform full **CRUD operations** on task items via RESTful APIs.

## 🚀 Features

- ✅ Create, Retrieve, Update, Delete (CRUD) tasks
- 🔐 RESTful endpoints using Django REST Framework
- 🧩 Class-Based Views & Serializers
- 🔄 JSON-based request and response handling
- 🗂️ SQLite3 as the default database

## 🛠️ Tech Stack

- Python 🐍
- Django 🌐
- Django REST Framework 🛠️
- SQLite (default DB)

## 📁 Project Structure

todo-list/
├── manage.py
├── todo/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
├── project_root/ # Settings, wsgi, urls
└── requirements.txt


## 📡 API Endpoints

| Method | Endpoint          | Description         |
|--------|-------------------|---------------------|
| GET    | `/api/todos/`     | List all tasks      |
| POST   | `/api/todos/`     | Create a new task   |
| GET    | `/api/todos/<id>` | Retrieve task by ID |
| PUT    | `/api/todos/<id>` | Update task         |
| DELETE | `/api/todos/<id>` | Delete task         |

## ▶️ Getting Started

1. **Clone the repository**
git clone https://github.com/ShailyBhargava/todo-api-django.git
cd todo-api-django

2. python -m venv venv
venv\Scripts\activate   # On Windows

3. pip install -r requirements.txt

4. python manage.py migrate

5. python manage.py runserver


📌 Notes
This project is for learning purpose and can be extended with user authentication, frontend integration, etc.

Make sure to configure .env file for production (not included in GitHub).

👩‍💻 Author
Shaily Bhargava
Backend Developer | Python & Django Enthusiast

