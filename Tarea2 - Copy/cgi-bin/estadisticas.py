#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Content-type: text/html\r\n\r\n')
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
with open('htmls/template.html', 'r') as file:
    s = file.read()

    print(s.format('Estadisticas Avistamientos', """
    <div class="volver">
    <button id="volverAPortada" class="boton" onclick="location.href='index.py';">Volver a la portada</button>
</div>

<div>
    <ul class="lista">
        <li class="elemento">
            <div class="tituloGrafico">
                Cantidad de avistamientos por dia:
            </div>
            <div class="grafico">
                <img id="estadistica1" src="../Fotos/FotosEstadisticas/Estadistica1.jpg" alt="Simply Easy Learning"
                     width="600" height="240">
            </div>
        </li>
        <li class="elemento">
            <div class="tituloGrafico">
                Cantidad de avistamientos por dia:
            </div>
            <div class="grafico">
                <img id="estadistica2" src="../Fotos/FotosEstadisticas/Estadistica2.jpg" alt="Simply Easy Learning"
                     width="400" height="400">
            </div>
        </li>
        <li class="elemento">
            <div class="tituloGrafico">
                Cantidad de avistamientos por dia:
            </div>
            <div class="grafico">
                <img id="estadistica3" src="../Fotos/FotosEstadisticas/Estadistica3.jpg" alt="Simply Easy Learning"
                     width="700" height="240">
            </div>
        </li>
    </ul>
</div>
    """,''),file=utf8stdout)
    #Ese ,'' es porque no se por que el template me tomaba la tupla del template con 3 elementos