# Sticky Notes App

Name: Mian Ayaan
Roll Number: 22p9149
Assignment: Web Engineering Assignment 2
University: FAST NUCES Peshawar

## About

A sticky notes app made with Django for the web engineering assignment. Users can register, login and manage their own notes. Each note has a color that shows as the card background.They can also eidt and delete the existing notes

## Features

- Register and login
- Each user can only see their own notes
- Create, edit and delete notes
- Color picker for notes
- Pin notes to the top
- Search by title or content
- 10 notes per page

## How to Run

1. Install django
pip install django

2. Go to project folder
cd stickynotes_22p9149

3. Run migrations
python manage.py migrate

4. Start server
python manage.py runserver

5. Open browser and go to
http://127.0.0.1:8000/register/

## URLs

/notes/ - note list
/notes/new/ - create note
/notes/<id>/edit/ - edit note
/notes/<id>/delete/ - delete note
/register/ - register
/login/ - login
/logout/ - logout
