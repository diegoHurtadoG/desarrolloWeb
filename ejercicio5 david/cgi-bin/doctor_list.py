#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
import manage_db

db = manage_db.ManageDB('localhost', 'root', '', 'ejercicio4')
cgitb.enable()

print("Content-type:text/html")
print("")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
doctors = db.get_doctors()

if not doctors:
    output = "<p> No hay doctores disponibles :( </p>"
else:
    rows = ""
    for doctor in doctors:
        id_col = f"<td>{doctor['id']}</td>"
        name_col = f"<td>{doctor['name']}</td>"
        experience_col = f"<td>{doctor['experience']}</td>"
        speciality_col = f"<td>{doctor['speciality']}</td>"
        email_col = f"<td>{doctor['email']}</td>"
        cellphone_col = f"<td>{doctor['cellphone']}</td>"
        photo_col = f"""<td><img src="./{doctor['photo_path']}" alt="{doctor['photo_name']}"></td>"""
        rows += f"""
           <tr>{id_col}{name_col}{experience_col}{speciality_col}{email_col}{cellphone_col}{photo_col}</tr>
        """
    output = f"""
    <table>
      <tr>
        <th>ID</th><th> Nombre </th><th> Experiencia </th><th> Especialidad </th><th> Correo </th><th> Celular </th><th> Foto </th>
      </tr>
      {rows}
    </table>
    """



print(output, file=utf8stdout)
