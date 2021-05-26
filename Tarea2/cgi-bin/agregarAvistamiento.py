#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-Type: text/html; charset=utf-8\r\n\r\n")
#print("Content-Type: text/html\r\n\r\n")

with open('htmls/template.html', 'r', encoding='utf-8') as file:
    s = file.read()

    print(s.format('Agregar Avistamiento', '''
<div class="titulo"> Formulario</div>

<div class="volver">
    <button id="volverAPortada" class="boton" onclick="location.href='index.py';">Volver a la portada</button>
</div>

<div id="erroresusuario"></div>
<div id="form">
    <form id="formulario" class="formulario" method="post" action="guardar_avistamiento.py" enctype="multipart/form-data">
        <!-- LUGAR  -->
        <div class = "datos">
        <h4>**Por ahora se cae si uno agrega un campo de foto y no le pone una foto, no se si alcanze a arreglarlo 
        para cuando la persona lea esto**</h4>
        </div>
        <div class="datos">
            <div class="instruccion">Region:</div>
            <select id="regiones" name="region"></select>
        </div>

        <div class="datos">
            <div class="instruccion">Comuna:</div>
            <select id="comunas" name="comuna"></select>
        </div>

        <div class="datos">
            <div class="instruccion">Sector:</div>
            <input id="inputSector" type="text" name="sector" value="" maxlength="100"/>
        </div>

        <!-- CONTACTO  -->

        <div class="datos">
            <div class="instruccion">Nombre:</div>
            <input id="inputNombre" type="text" name="nombre" value="" size="100" maxlength="200"/>
        </div>

        <div class="datos">
            <div class="instruccion">Correo Electronico:</div>
            <input id="inputEmail" type="email" name="email" value="" size="100"/>
        </div>

        <div class="datos">
            <div class="instruccion">Numero de celular:</div>
            <input id="inputCelular" type="tel" name="celular" value="" size="15" placeholder="+569 12345678"/>
        </div>

        <!-- INFORMACION  -->
        <div class="divInformacionAvistamiento">
            <div class="datos informacionAvistamiento">
                <div class="instruccion">Dia y Hora:</div>
                <input id="inputDHA" type="datetime-local" name="dia-hora-avistamiento" value="" size="20"
                       required="required"/>
            </div>

            <div class="datos informacionAvistamiento">
                <div class="instruccion">Tipo:</div>
                <select id="inputTA" name="tipo-avistamiento">
                    <option value="no sé">No sé</option>
                    <option value="insecto">Insecto</option>
                    <option value="arácnido">Arácnido</option>
                    <option value="miriápodo">Miriápodo</option>
                </select>
            </div>

            <div class="datos informacionAvistamiento">
                <div class="instruccion">Estado:</div>
                <select id="inputEA" name="estado-avistamiento">
                    <option value="no sé">No sé</option>
                    <option value="vivo">Vivo</option>
                    <option value="muerto">Muerto</option>
                </select>
            </div>

            <div class="datos informacionAvistamiento" id="divFotos">
                <div class="instruccion">Fotos:</div>
                <button id="agregaFoto" class="boton" onclick="agregarFoto('')">Agregar Foto</button>
                <input type="hidden" id="cantidadFotos" name="cantidad-fotos-avistamiento" value="1"> <!-- A este le sumo 1 en cada agregarFoto('') -->
                <br>
                <input id="inputFA" type="file" name="fotos-avistamiento"/> <br>

            </div>
        </div>

        <div class="datos divInformacionAvistamiento avistamientosExtra" id="divAvistamientosExtra">


        </div>

        <div class="entrada botones">
            <button id="nuevoAvistamientoButton" type="button" class="boton" onclick="agregarAvistamiento()">Informar
                otro avistamiento en este sector
            </button>
            <br>
            <button id="enviar" class="boton" type="button" onclick="pedirConfirmacion()">Enviar informacion de
                avistamiento(s)
            </button>
            <br>

            <div class="botonInvisible" id="botonesInvisibles">
               <!-- <button id="confirmarBoton" class="boton" type="submit">Si, Estoy seguro que quiero confirmar</button> -->
                <button id="confimarBoton" class="boton" type="button" onclick="receive_json()">Si, confirmar</button>
                <button id="rechazarBoton" class="boton" type="button" onclick="esconderConfirmacion()">No estoy seguro, volver</button>
            </div>
        </div>

    </form>
</div>
    ''', ''))

    #Agregar de ahi puede ser en template o aqui arriba las weas de validacion (scripts)
    #Si no funciona por Index puede ser por la tupla de 3