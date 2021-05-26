#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html\r\n\r\n")

with open('htmls/template.html', 'r', encoding='utf-8') as file:
    s = file.read()

    print(s.format('Detalle Avistamiento', '''
<div class="caracteristicas">
    <ul class="lista" id="listaDetalles">
    <h5> Vale decir que en mi archivo db.py esta la consulta que retorna toda la info necesaria. <br>
    Esta info logre obtenerla desde la lista, pero me falto la parte de poder mandarla a esta visualizacion <br>
    Tengo la idea de hacer un JSON, mandarlo al handler de las filas, y que este se lo mande al .py que <br>
    despliega esta pagina, pero me falto tiempo para hacerlo porque tuve un problema que me duro <br>
    como 4 dias y al final nunca le encontre solucion y tuve que hacer todo el submit denuevo :( <br>
    Perdon por tan poco, me organize mal en la semana de receso</h5>
        <li class="elemento">
            Contacto: <br>
            <ul>
                <li class="lineaInformacion">
                    Nombre: Aqui va el nombre
                </li>
                <li class="lineaInformacion">
                    Mail: Aqui va el mail
                </li>
                <li class="lineaInformacion">
                    Numero: Aqui va el numero
                </li>
            </ul>
        </li>
        <li class="elemento">
            Lugar: <br>
            <ul>
                <li class="lineaInformacion">
                    Region: Aqui va la region
                </li>
                <li class="lineaInformacion">
                    Comuna: Aqui va la comuna
                </li>
                <li class="lineaInformacion">
                    Sector: Aqui va el sector
                </li>
            </ul>
        </li>
        <li class="elemento">
            Avistamiento: <br>
            <ul>
                <li class="lineaInformacion">
                    Tipo: Aqui va el tipo
                </li>
                <li class="lineaInformacion">
                    Estado: Aqui va el estado
                </li>
                <li class="lineaInformacion">
                    Dia y Hora: Aqui va dia y hora
                </li>
                <li class="lineaInformacion">
                    Fotos: Aqui van las fotos
                </li>
            </ul>
        </li>
    </ul>
</div>

<div class="botones">
    <button id="volverAListado" class="boton" onclick="location.href='listadoAvistamientos.py';">Volver a Lista
    </button>
    <button id="volverAPortada" class="boton" onclick="location.href='index.py';">Volver a Portada</button>
</div>

    ''', ''))