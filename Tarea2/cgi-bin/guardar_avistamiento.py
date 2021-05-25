#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb; cgitb.enable()
import os
import db

print("Content-type:text/html\r\n\r\n")

with open('htmls/template.html', 'r') as file:
    s = file.read()

    form = cgi.FieldStorage()
    avdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")

    # Aqui hay documentacion de como manejar el fieldStorage del cgi y obtener los valores
    # https://docs.python.org/3/library/cgi.html
    data = (
        form['region'].value, form['comuna'].value, form['sector'].value,
        form['nombre'].value, form['email'].value, form['celular'].value,
        form.getlist('dia-hora-avistamiento'), form.getlist('tipo-avistamiento'), form.getlist('estado-avistamiento'),
        form['fotos-avistamiento'] # Ver bien si los archivos los llamo con getlist o con form[''], sin el .value (o con, revisar ejercicio)
    )
    avdb.save_avistamiento(data)

    html = f'''

    <div class="titulo"><h2>Avistamiento guardado!</h2></div>
    <div>


            Su mensaje informacion se guardo con exito!!!


    </div>

    <div class="volver">
        <button id="volverALista" class="boton" onclick="location.href='listadoAvistamientos.py';">Volver a la portada</button>
    </div>


    '''

    print(s.format('Informacion guardada', html, ''))
