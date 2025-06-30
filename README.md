# 📝 To-Do App (Django)

A clean, user-friendly To-Do list web application built with Django. Users can sign up, log in, add, update, and delete tasks — all with a minimal and responsive interface. Hosted on [Render](https://render.com).

---

## 🚀 Features

- User authentication (signup & login)
- Add, edit, and delete tasks
- Task color-coding based on completion status
- Persistent tasks per user
- Responsive UI using custom CSS
- Deployed live on Render

---

## 🔧 Tech Stack

- Python 3.12
- Django
- SQLite3 (default)
- HTML, CSS (custom)
- Font Awesome (icons)
- Gunicorn + WhiteNoise (for deployment)

---

## 📁 Project Structure

```
.
├── templates/             # All HTML templates
│   ├── login.html
│   ├── signup.html
│   ├── todo.html
│   └── todo_edit.html
├── to_do/                 # Main Django app
│   ├── static/            # CSS + JS files
│   │   ├── css/
│   │   └── js/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── Procfile               # For Render deployment
└── README.md
```

---

## 🛠️ Setup Instructions (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/hey-granth/to-do.git
   cd to-do
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. Visit `http://127.0.0.1:8000`

---

## 🌐 Deployment on Render

1. Push to GitHub
2. Add a `Procfile`:
   ```
   web: gunicorn to_do.wsgi:application --bind 0.0.0.0:$PORT
   ```
3. Add optional `build.sh` to run:
   ```bash
   python manage.py collectstatic --no-input
   python manage.py migrate
   ```

4. Set up Render Web Service:
    - Build Command: `./build.sh`
    - Start Command: `gunicorn to_do.wsgi:application --bind 0.0.0.0:$PORT`

5. Add environment variables:
    - `DJANGO_ALLOWED_HOSTS=your-app.onrender.com`
    - `DJANGO_SECRET_KEY=your-secret-key`
    - `DEBUG=False`

---

## ✨ Live Demo

🔗 [Live Link](https://to-do-q0fr.onrender.com/)

---

## 🧑‍💻 Author

**Granth Agarwal**  
GitHub: [@hey-granth](https://github.com/hey-granth)

--- 

## 📃 License

This project is open source under the MIT License.
