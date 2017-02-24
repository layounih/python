
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bottle import route, run


@route('/')
def index():
    return 'Hello world!!'


run(host='localhost', port=8080)