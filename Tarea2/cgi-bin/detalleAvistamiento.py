#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html; charset=utf-8\r\n\r\n")

with open('htmls/template.html', 'r') as file:
    s = file.read()

    print(s.format('Detalle Avistamiento', '''
<div class="caracteristicas">
    <ul class="lista" id="listaDetalles">
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