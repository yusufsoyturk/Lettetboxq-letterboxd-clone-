# 🎬 Letterboxq

Letterboxq is a Django web application inspired by the popular movie platform Letterboxd. It allows users to log the movies they have watched, rate them, write reviews, and follow reviews from other users.

## 🚀 About the Project

This project aims to build social interaction around a movie database. Users can create their own digital movie diaries, rate movies on a scale of 1-10, and leave comments.

**Key Feature:** With dynamic button management, users can **delete** their own comments on the "Reviews" page, while seeing a **"Log" (Add to List)** button on other users' comments to quickly add that movie to their own diaries.

## ✨ Features

* **User Authentication:** Sign Up, Login, and Logout operations.
* **Movie Listing:** Listing movies from the database with posters, summaries, and general rating information.
* **Movie Logging:**
    * Adding movies to the "Watched" list.
    * 1-10 rating system.
    * Writing personal comments/reviews.
* **Profile Page:**
    * Users view only the movies they have watched.
    * Viewing own comments and ratings.
    * Ability to delete records from the database.
* **Reviews Feed:**
    * Listing reviews from all users (newest to oldest).
    * **Smart Action Buttons:**
        * *If it's your comment:* **DELETE** button appears.
        * *If it's someone else's comment:* **+ LOG** button appears (Allows you to add the movie to your own list).

## 🛠️ Technologies

This project was developed using the following technologies:

* **Language:** Python 3.12.3
* **Framework:** Django 4.2.11
* **Database:** SQLite (For development)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Template Engine:** Django Templating Engine

## ⚙️ Installation and Setup

Follow the steps below to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/letterboxq.git](https://github.com/YOUR_USERNAME/letterboxq.git)
cd letterboxq
```

### 2. Create a Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Django
```bash
pip install django==4.2.11
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```
