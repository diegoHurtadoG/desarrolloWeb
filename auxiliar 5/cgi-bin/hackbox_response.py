#!/opt/homebrew/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-


import cgi
from save_data import HackBoxDatabase

print('Content-type: text/html\r\n\r\n')

form = cgi.FieldStorage()
hbdb = HackBoxDatabase('root', '')

data = (
    form['nombre'].value, form['edad'].value, form['comentario'].value, form['file']
)

hbdb.save_data(data)

with open('static/template.html', 'r') as file:
    s = file.read()
    print(s.format('Hackbox - home', 'Su mensaje información se guardó correctamente!'))
