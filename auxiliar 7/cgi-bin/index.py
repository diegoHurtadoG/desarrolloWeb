#!/opt/homebrew/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os
import html
from utils import imprimeerror
from http import cookies

cgitb.enable()

# Obtener las cookies
c = ''
if 'HTTP_COOKIE' in os.environ:
    c = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])


def validar_cookie(ck: 'cookies.SimpleCookie') -> bool:
    """
    Valida la cookie del usuario.

    cookie = {
        "login": "username=xxx, status=true",
    }

    :param ck: Cookie
    :return: True si usuario inicio sesión
    """
    if 'login' not in ck.keys():
        return False
    b = ck['login'].value.split(', ')
    if 'username=' not in b[0]:
        return False
    if 'status=' not in b[1]:
        return False
    # uname = b[0].replace('username=', '')
    status = b[1].replace('status=', '')
    return status == 'true'


# Lista de sesiones validas
valid_users = {
    'pablo': '1234',
    'admin': 'hola'
}

# Leemos desde el cliente cuando inicia sesion
login_form = cgi.FieldStorage()
if 'username' in login_form and 'pass' in login_form:
    u_name = html.escape(login_form.getvalue('username'))
    u_pass = html.escape(login_form.getvalue('pass'))
    if u_name in valid_users.keys() and valid_users[u_name] == u_pass:
        cookie = cookies.SimpleCookie()
        cookie['login'] = 'username={0}, status=true'.format(u_name)
        cookie['login']['max-age'] = 10000  # segundos
        c = cookie
        print(cookie)
    else:
        imprimeerror(99, 'El usuario o la contraseña son incorrectos')

print('Content-type: text/html\r\n\r\n')

if len(c) == 0 or not validar_cookie(c):
    with open('static/template.html', 'r', encoding='utf-8') as file:
        s = file.read()
        print(s.format('Hackbox - login', f"""
        <form id="miformulario" method="post">

            <div class="entrada">

                <div class="leyenda">User</div>

                <input type="text" id="nombre" name="username" minlength="4" maxlength="100" required="required"
                       placeholder="Username"/>

            </div>

            <div class="entrada">

                <div class="leyenda">Password</div>

                <input type="password" name="pass" size="10" maxlength="10">

            </div>

            <div class="entrada botones">

                <button id="enviar" type="submit">Submit</button>

                <button id="borrar" type="reset">Borrar</button>

            </div>

        </form>
        """))

else:
    with open('static/template.html', 'r', encoding='utf-8') as file:
        s = file.read()
        print(s.format('Hackbox - home', f"""
        <div class="saludo">Bienvenido, @{c['login'].value.split(',')[0].replace('username=', '')}</div>
        <form id="miformulario" method="post"
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
    
                <input type="file" id="archivo" name="file" accept="application/pdf">
    
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
