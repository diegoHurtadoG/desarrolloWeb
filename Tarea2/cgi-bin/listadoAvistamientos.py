#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db



hbdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")
data = hbdb.get_lista_avistamientos()

print("Content-Type: text/html; charset=utf-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)


with open('htmls/template.html', 'r', encoding='utf-8') as file:
    s = file.read()

    preTabla = f'''
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
            <tr onclick="rowHandler(this)"> <!-- Aqui podria pasarle como segundo parametro un self.get_info_av(d[0]) -->
                <td>{str(d[1])}</td>
                <td>{str(d[2])}</td>
                <td>{str(d[3])}</td>
                <td>{str(d[4])}</td>
                <td>{hbdb.get_total_avistamientos(d[0])}</td>
                <td>{hbdb.get_total_fotos(d[0])}</td>
            </tr>
        '''
        tabla += row

    tabla += '</table>\n</div>'

    print(s.format('Listado Avistamientos', preTabla + tabla, ''),file=utf8stdout)
