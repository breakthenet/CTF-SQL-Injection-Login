from django.http import HttpResponse
import datetime
import json
from django.template.response import TemplateResponse
import os
from game.errors import ChallengeError
from django.db import connections
import hashlib

def start_hack(request):
    return TemplateResponse(request, 'sql_inject_login.html', context={})

def submit_attempt(request):
    try:
        results = _submit_test(request.POST)
        return HttpResponse(json.dumps(results, default=json_custom_parser), content_type='application/json', status=200)
    except ChallengeError as e:
        return HttpResponse(json.dumps(e.serialize(), default=json_custom_parser), content_type='application/json', status=400)

def _submit_test(post_data):
    username = post_data['username']
    difficulty = post_data['difficulty'] #['Easy', 'Medium', 'Hard']

    challenge_meta = {}
    password = hashlib.md5(post_data['password']).hexdigest()
    challenge_meta['query'] = "SELECT username from game_user WHERE username='{username}' AND password='{password}'"

    challenge_meta['filters'] = [';']
    if difficulty == 'Medium':
        challenge_meta['filters'] = [';', '"', '-', '\\', 'union', 'select', 'from', 'having', '&', '=', '|']
    if difficulty == 'Hard':
        challenge_meta['filters'] = [';', '"', "\\", " ", "and", "where", "limit", "null", "union", "select", "from", "having", "&", "=", "|", "-"] #Consider also adding "/", "or"

    for filt in challenge_meta['filters']:
        username = username.replace(filt, '')

    print "Filters active:", challenge_meta['filters']

    query = challenge_meta['query'].replace("{username}", username)
    query = query.replace("{password}", password)

    print "Query attempt:", query

    try:
        cursor = connections['default'].cursor()
        cursor.execute(query)
        keys = [col[0] for col in cursor.description]
        results = [
            dict(zip(keys, row))
            for row in cursor.fetchall()
        ]

        match_found = False
        username = ""
        ctf_flag = ''
        if len(results) > 0:
            for r in results:
                if r.get('username'):
                    print "SUCCESS with query", query, challenge_meta['filters']
                    ctf_flag = os.environ.get('CTF_FLAG_'+difficulty.upper())
                    match_found = True
                    username = r.get('username')

    except Exception as e:
        print "submit_attempt error", str(e)

        raise ChallengeError(query, etype="Invalid Syntax")

    finally:
        cursor.close()


    return {
        'ctf_flag': ctf_flag,
        "match_found": match_found,
        "username": username
    }


def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)