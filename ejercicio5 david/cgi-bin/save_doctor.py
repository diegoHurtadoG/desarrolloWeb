#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
import manage_db

print("Content-type:text/html")
print("")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

db = manage_db.ManageDB('localhost', 'root', '', 'ejercicio4')
cgitb.enable()

form = cgi.FieldStorage()
speciality = form.getfirst('especialidad-medico')
# pattern matching lova <3
[photo] = form['foto-medico'] if isinstance(form['foto-medico'], list) else [form['foto-medico']]
name = form.getfirst('nombre-medico')
experience = form.getfirst('experiencia-medico')
email = form.getfirst('email-medico')
cellphone = form.getfirst('celular-medico')

photo_name = photo.filename
photo_hashed_name = f'{db.count_doctors() + 1}_{hash(photo_name)}'
photo_path = f'media/{photo_hashed_name}'

fp = open(photo_path, 'wb')
fp.write(photo.file.read())
fp.close()
photo_id = db.insert_photo(photo_name, photo_path)
db.insert_doctor(cellphone, email, speciality, experience, name, photo_id)



body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Datos agregados</title>
    <link rel="stylesheet" type="text/css" href="./../style.css" />
</head>
<body>
    <ul class="topnav">
      <li><a class="active" href="../index.html">Inicio</a></li>
      <li><a href="../add_doctor.html">Agregar Datos de Médico</a></li>
    </ul>
    <div class="titulo negrita">
        Datos agregados
    </div>
    <div id="main">
        <p>Los datos fueron enviados con éxito!</p>
        <replace>
    </div>
</body>
"""

print(body, file=utf8stdout)
