** INSTALL VIRTURL ENVIROMENT WITH PIPENV **
- pip install pipenv
- pipenv install requests
- pipenv shell
- pipenv freeze
- python -m pip freeze

** Create execuable python sys **
- python
- >>> import sys
- >>> print(sys.executable)
- >>> exit()

*** Use pipenv ***
*cd project has Pipfile and Pipfile.lock folder and run commend*
- pipenv install
- pipenv shell

** FINAL - Go to project folder to working **
- django-admin startproject blogsite 
- cd blogsite
- pip install django-ckeditor
- pip install -U selenium
- python manage.py migrate
- python manage.py runserver
** or user orther host setting **
- python manage.py runserver 127.0.0.1:8001 --settings=blogsite.settings

** Make app **
python manage.py startapp blog
** add module blog to setting file **
** Make model, makemigrations, migrate **
** Register into admin.py **
admin.site.register(Post)

*** Make supper admin **
- python manage.py createsuperuser
** admin/admin **

** Redis connection
>>> import redis
>>> r= redis.Redis(host='**.**.**.**', port=6379, password='***', db=1)
>>> r.set('foo','bar')
>>> r.get('foo')
>>> r.lastsave()