#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb; cgitb.enable()
import db

print("Content-Type: text/html; charset=utf-8\r\n\r\n")

form = cgi.FieldStorage()
avdb = db.Avistamiento('localhost', 'cc500221_u', "sellusplac", "cc500221_db")

# Aqui hay documentacion de como manejar el fieldStorage del cgi y obtener los valores
# https://docs.python.org/3/library/cgi.html
data = (
    form['region'].value, form['comuna'].value, form['sector'].value,
    form['nombre'].value, form['email'].value, form['celular'].value,
    form.getlist('dia-hora-avistamiento'), form.getlist('tipo-avistamiento'), form.getlist('estado-avistamiento'),
    form['fotos-avistamiento'], # Ver bien si los archivos los llamo con getlist o con form[''], sin el .value (o con, revisar ejercicio)
    form.getlist('cantidad-fotos-avistamiento')
)
#Idea de ultima mano: No agregar las fotos al data de arriba, y como tendriamos la lista de fotos por avistamiento
#   podria separar los names de los input de foto y llamarlas a cada una por nombre dependiendo de cuantos
#   avistamientos tuve, ejemplo: form['fotos-avistamiento1'], form['fotos-avistamiento2']
#   tendria que cambiarles los nombres a los que agrego y al que viene
avdb.save_avistamiento(data)