#!/usr/bin/python3
# -*- coding: utf-8 -*-

from save_data import HackBoxDatabase

hbdb = HackBoxDatabase('root', '')
data = hbdb.get_all('usuario')

print('Content-type: text/html\r\n\r\n')

with open('../htmls/template.html', 'r') as file:
    s = file.read()

    strPreTabla = f'''
    <div class="titulo"><h1>Bienvenid@!</h1></div>

<div>
    <ul class="lista">
        <li class="elemento">
            <button id="informarAvistamientoIndex" class="boton" onclick="location.href='agregarAvistamiento.html';">
                Nuevo
                Avistamiento
            </button>
        </li>
        <li class="elemento">
            <button id="verListadoAvistamientosIndex" class="boton"
                    onclick="location.href='listadoAvistamientos.html';">Ver
                Listado
                de Avistamientos
            </button>
        </li>
        <li class="elemento">
            <button id="verEstadisticasIndex" class="boton" onclick="location.href='estadisticas.html';">Ver
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
        row = f'''
            <tr>
                <td>{str(d[1])}</td>
                <td>{str(d[2])}</td>
                <td>{str(d[3])}</td>
                <td>{str(d[4])}</td>
                <td>{str(d[5])}</td>
            </tr>
        '''
        tabla += row

    tabla += '</table>\n</div>'

    print(s.format('Portada Bichometro', strPreTabla + tabla))
    #Si no funciona por indexError, agregar un .'' en el format como en estadisticas.py