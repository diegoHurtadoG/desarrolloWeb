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
                        Cantidad de avistamientos por dia (Cantidad avistamientos v/s Fecha del año): </br>
                        </div>
                        <div>
                        *Disclaimer: (No sabia si hacerlo asi o por dia de la semana, </br>
                        pero encontre mas util un grafico de esta forma en caso de ser un proyecto real, quiza con </br>
                        otra forma de escribir las fechas o otro intervalo, pero no hay tiempo para lujos :( ...)
                        </div>
                        <div class="grafico">
                            <div id='grafico1' style='height: 240px;width: 800px;'></div>
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
                        Estados de avistamientos por mes (Cantidad de avistamiento v/s Numero del mes): </br>
                        </div>
                        <div class="grafico">
                            <div id='grafico3' style='height: 240px;width: 800px;'></div>
                        </div>
                    </li>
                    
                </ul>
        </div>

    </div>
    """, ''), file=utf8stdout)
    # Ese ,'' es porque no se por que el template me tomaba la tupla del template con 3 elementos
