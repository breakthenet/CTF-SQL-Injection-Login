import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import django
django.setup()

from django.db import connections

if not os.environ.get('IS_HEROKU_SERVER', False):
    os.system("dropdb sqlinjlogin")
    os.system("createdb sqlinjlogin")

os.system("python manage.py migrate")

insert_data = """
INSERT INTO "game_user" ("username", "password") VALUES ('admin', '{password}')
"""
insert_data = insert_data.replace("{password}", os.environ.get('CTF_FLAG_EASY')+os.environ.get('CTF_FLAG_MEDIUM')+os.environ.get('CTF_FLAG_HARD'))

try:
    cursor = connections['default'].cursor()
    cursor.execute(insert_data)
finally:
    try:
        cursor.close()
    except:
        pass