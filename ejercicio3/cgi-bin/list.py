#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb;

cgitb.enable()
import mysql.connector
import db

print("Content-type: text/html\r\n\r\n")

hbdb = db.Doctor("localhost", "root", "admin", "ejercicio3")
data = hbdb.get_doctors()

head = '''
    <!DOCTYPE html>
<!--suppress ALL -->
<head>
    <meta charset="UTF-8">
    <title>Doctores</title>
    <link rel="stylesheet" type="text/css" href="../style.css">

    <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
'''
b1 = '''
<body>

<div class="menu entrada">

    <div class="entrada">
        <a href="https://google.cl">Home</a>
    </div>


</div>

<div class="titulo negrita">Doctores</div>
<div class="main">



        <table>
        <tr>
    <th>Nombre</th>
    <th>Experiencia</th>
    <th>Especialidad </th>
    <th>Email </th>
    <th>Celular </th>
    <th>Foto</th>
'''
print(head)
print(b1)

for d in data:
    row = f'''
            <tr>
                <th>{str(d[1])}</th>
                <th>{str(d[2])}</th>
                <th>{str(d[3])}</th>
                <th>{str(d[4])}</th>
                <th>{str(d[5])}</th>
                <th><img src='/media/{str(d[6])}.jpg' alt='Imagen doctor {str(d[0])}' style="max-height: 120px;max-width: 120px;" ></th>
            </tr>
        '''
    print(row)

b2 = '''
</table>


</div>

<div id="error">Este es un mensaje de error</div>

</body>


</html>
'''
print(b2)
