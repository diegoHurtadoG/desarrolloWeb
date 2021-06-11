#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Content-type: text/html\r\n\r\n')
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
with open('htmls/estadisticas.html', 'r') as file:
    s = file.read()

    print(s.format('Estadisticas Avistamientos', """
    <div class="volver">
    <button id="volverAPortada" class="boton" onclick="location.href='../cgi-bin/index.py';">Volver a la portada</button>
    </div>
    <div id="main">
        <div>
                <ul class = lista>
                    <li class="elemento">
                        <div class="tituloGrafico">
                        Cantidad de avistamientos por dia: (No sabia si hacerlo asi o por dia de la semana, </br>
                        pero encontre mas util un grafico de esta forma en caso de ser un proyecto real)
                        </div>
                        <div class="grafico">
                            <div id='grafico1' style='height: 240px;width: 600px;'></div>
                        </div>
                    </li>
                
                    <li class="elemento">
                        <div class="tituloGrafico">
                        Cantidad de avistamientos por tipo:
                        </div>
                        <div class="grafico">
                            <div id='grafico2' style='height: 400px;width: 400px;'></div>
                        </div>
                    </li>
                
                    <li class="elemento">
                        <div class="tituloGrafico">
                        Estados de avistamientos por mes:
                        </div>
                        <div class="grafico">
                            <div id='grafico2' style='height: 240px;width: 700px;'></div>
                            <img id="estadistica3" src="../Fotos/FotosEstadisticas/Estadistica3.jpg" alt="Simply Easy Learning"
                             width="700" height="240">
                        </div>
                    </li>
                    
                </ul>
        </div>

    </div>
    """, ''), file=utf8stdout)
    # Ese ,'' es porque no se por que el template me tomaba la tupla del template con 3 elementos
