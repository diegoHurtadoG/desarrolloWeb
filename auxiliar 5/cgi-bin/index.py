#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Content-type: text/html\r\n\r\n')

with open('static/template.html', 'r') as file:
    s = file.read()
    print(s.format('Hackbox - home', """
    <form id="miformulario" method="post" action="hackbox_response.py"
          onsubmit="return validacionFormulario()"
          enctype="multipart/form-data"
          >

        <div class="entrada">

            <div class="leyenda">Nombre</div>

            <input type="text" id="nombre" name="nombre" minlength="4" maxlength="100" required="required"
                   placeholder="Escriba su nombre"/>

        </div>

        <div class="entrada">

            <div class="leyenda">Edad</div>

            <input type="number" id="edad" name="edad" size="10" maxlength="10">

        </div>
        
        <div class="entrada">

            <div class="leyenda">Archivo</div>

            <input type="file" id="archivo" name='file' accept='application/pdf'>

        </div>


        <div class="entrada">

            <div class="leyenda comentario" style='vertical-align: top;'>Comentario</div>

            <textarea id="comentario" name="comentario" maxlength="1000" rows="10" cols="40"
                      placeholder="Ingrese sus comentarios acá"></textarea>

        </div>

        <div class="entrada botones">

            <button id="enviar" type="submit">Submit</button>

            <button id="borrar" type="reset">Borrar</button>

        </div>

    </form>
    """))
