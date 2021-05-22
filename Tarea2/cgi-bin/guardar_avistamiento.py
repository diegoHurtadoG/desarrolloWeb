#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb;cgitb.enable()

import db


print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()
avdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")


data = (
    form['region'].value, form['comuna'].value, form['sector'].value,
    form['nombre'].value, form['email'].value, form['celular'],
    form['dia-hora-avistamiento'], form['tipo-avistamiento'], form['estado-avistamiento'], form['fotos-avistamiento']
)
avdb.save_avistamiento(data)

html = f'''
    <!DOCTYPE html>
<!--suppress ALL -->
<head>
    <meta charset="UTF-8">
    <title>Avistamientos</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>


<body>

<div class="titulo"><h2>Avistamiento guardado!</h2></div>
<div>


        Su mensaje informacion se guardo con exito!!!


</div>

<div class="volver">
    <button id="volverALista" class="boton" onclick="location.href='cgi-bin/listadoAvistamientos.py';">Volver a la portada</button>
</div>

</body>

</html>
'''
print(html)
