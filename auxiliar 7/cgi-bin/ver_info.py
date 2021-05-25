#!/opt/homebrew/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

from save_data import HackBoxDatabase

print('Content-type: text/html\r\n\r\n')

hbdb = HackBoxDatabase('root', '')
data = hbdb.get_all('usuario')

with open('static/template.html', 'r') as file:
    s = file.read()

    # Creamos la tabla
    tabla = f'''
    <table>
    <tr>
        <th>Nombre</th>
        <th>Edad</th>
        <th>Comentario</th>
        <th>ID Archivo</th>
    </tr>
    '''

    for d in data:
        row = f'''
            <tr>
                <td>{str(d[1])}</td>
                <td>{str(d[2])}</td>
                <td>{str(d[3])}</td>
                <td>{str(d[4])}</td>
            </tr>
        '''
        tabla += row

    tabla += '</table>'

    print(s.format('Hackbox - Ver información', tabla))
