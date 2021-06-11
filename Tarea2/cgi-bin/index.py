#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db

hbdb = db.Avistamiento('localhost', 'cc500221_u', "sellusplac", "cc500221_db")
data = hbdb.get_lista_portada()

print("Content-Type: text/html; charset=utf-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

with open('../htmls/template.html', 'r', encoding='utf-8') as file:
    s = file.read()

    strPreTabla = f'''
    <div class="titulo"><h1>Bíenvenid@!</h1></div>

<div>
    <ul class="lista">
        <li class="elemento">
            <button id="informarAvistamientoIndex" class="boton" onclick="location.href='./agregarAvistamiento.py';">
                Nuevo
                Avistamiento
            </button>
        </li>
        <li class="elemento">
            <button id="verListadoAvistamientosIndex" class="boton"
                    onclick="location.href='./listadoAvistamientos.py';">Ver
                Listado
                de Avistamientos
            </button>
        </li>
        <li class="elemento">
            <button id="verEstadisticasIndex" class="boton" onclick="location.href='./estadisticas.py';">Ver
                Estadisticas
            </button>
        </li>
    </ul>
</div>
    '''

    tabla = f'''
<div class="tablaIndex">
<table class="tablaInformacion">
        <tr>
            <th>Fecha Hora</th>
            <th>Comuna</th>
            <th>Sector</th>
            <th>Tipo</th>
            <th>Total Fotos</th>
        </tr>
'''

    for d in data:
        paths_list = hbdb.get_fotos_portada(d[4])
        buff = ''
        for p in paths_list:
            p = str(p) # ('./Fotos/Avistamientos/8ecd2d532cb99989ad2c5e857912670.jpg',)
            p = p[2:len(p)-3] # ../Fotos/Avistamientos/8ecd2d532cb99989ad2c5e857912670.jpg
            buff += '<img src="' + p + '" alt="Foto Avistamiento" width="320" height="240">'
            # CUANDO CAMBIE A ANAKENA AQUI PROBABLEMENTE TIRE PROBLEMAS DE PATH
        row = f'''
            <tr>
                <td>{str(d[0])}</td>
                <td>{str(d[1])}</td>
                <td>{str(d[2])}</td>
                <td>{str(d[3])}</td>
                <td>{buff}</td>
            </tr>
        '''
        tabla += row

    tabla += '</table>\n</div>'

    print(s.format('Portada Bichometro', strPreTabla + tabla, ''), file=utf8stdout)
    #Si no funciona por indexError, agregar un .'' en el format como en estadisticas.py