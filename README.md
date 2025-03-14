# Django Blog Final Project
## How to Use
1) Clone and cd to cloned directory:
```
git clone https://github.com/giorgiabes/blog-starter.git && cd blog-starter
```
2) Create and activate a virtual environment:
```
python3 -m venv venv && source venv/bin/activate
```
3) Install the requirements:
```
pip install -r requirements.txt
```
4) Apply the migrations:
```
python manage.py migrate
```
5) Create Super User
```
python manage.py createsuperuser
```
6) Seed Fake Data
```
python manage.py seed_db
```
7) Run server
```
python manage.py runserver
```