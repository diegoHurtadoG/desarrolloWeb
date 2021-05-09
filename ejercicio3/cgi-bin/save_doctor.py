#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb;cgitb.enable()

import db



print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
hbdb = db.Doctor("localhost", "root", "admin", "ejercicio3")

data = (
    form['nombre-medico'].value, form['experiencia-medico'].value, form['especialidad-medico'].value,
    form['email-medico'].value, form['celular-medico'].value, form['foto-medico']
)
hbdb.save_doctor(data)

html = f'''
    <!DOCTYPE html>
<!--suppress ALL -->
<head>
    <meta charset="UTF-8">
    <title>Doctores</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>


<body>

<div class="menu entrada">

    <div class="entrada">
        <a href="https://google.cl">Home</a>
    </div>


</div>

<div class="titulo negrita">Doctores</div>
<div class="main">



        Su mensaje informacion se guardo con exito!!!



</div>



</body>


</html>
'''
print(html)
