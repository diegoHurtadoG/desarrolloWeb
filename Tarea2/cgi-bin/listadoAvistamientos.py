#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db

print("Content-type: text\html\r\n\r\n")

hbdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")
data = hbdb.get_lista_avistamientos()

with open('htmls/template.html', 'r') as file:
    s = file.read()

    preTabla=f'''
    <div class="botonDiv" id="informar">
        <!-- Lleva al usuario a agregar avistamiento -->
        <div class="volver2">
            <button id="informarAvistamiento" class="boton" onclick="location.href='agregarAvistamiento.py';">Nuevo Avistamiento</button>
            <button id="volverAPortada" class="boton" onclick="location.href='index.py';">Volver a la portada</button>
        </div>
    </div>
    '''

    tabla = f'''
    <div class="tabla" id="tablaDiv">
    <table id="tablaAvistamientos" class="tablaInformacion">
        <tr>
            <th>Fecha Hora</th>
            <th>Comuna</th>
            <th>Sector</th>
            <th>Nombre Contacto</th>
            <th>Total Avistamientos</th>
            <th>Total Fotos</th>
        </tr>
    '''

    for d in data:
        row = f'''
            <tr>
                <td>{str(d[1])}</td>
                <td>{str(d[2])}</td>
                <td>{str(d[3])}</td>
                <td>{str(d[4])}</td>
                <td>{str(d[5])}</td>
                <td>{str(d[6])}</td>
            </tr>
        '''
        tabla += row

    tabla += '</table>\n</div>'

    print(s.format('Listado Avistamientos', preTabla + tabla, ''))
    #Si falla puede ser por la tupla de 3 elementos en el format.
