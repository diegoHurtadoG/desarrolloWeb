#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb

cgitb.enable()

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

head = '''
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio 3</title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="style.css" />    <!-- CSS: -->
</head>
'''

body = f"""
<body>

<div class="titulo negrita ">Doctor agregado!</div>


<div id="main">

    <p>El doctor ha sido guardado con exito!</p>
"""

footer = f"""

</div>


</body>

"""

form = cgi.FieldStorage()
print(head, file=utf8stdout)

print(body, file=utf8stdout)



for key in form.keys():
    print("<p>" + key + " : " + form[key].value + "</p>", file=utf8stdout)
print(footer, file=utf8stdout)