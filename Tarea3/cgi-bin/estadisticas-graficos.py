#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db

hbdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")

# Aqui tengo que obtener la data para los graficos y guardarlas en variables, estilo
data_graf1 = hbdb.get_cantidad_por_dia()  # Tipo list
data_graf2 = hbdb.get_cantidad_por_tipo()  # Tipo list
data_graf3 = hbdb.get_cantidad_mensual_por_estado()  # Tipo list

print('Content-type: text/html\r\n\r\n')
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

# La idea aqui es imprimir la infor de arriba de forma conveniente cosa de
#   agarrarla en el ajax.js y trabajarla
# Para plotear los graficos, en el ejemplo donde sale #placeholder es el id de donde quiero poner el grafico
#   asique cada grafico lo pongo en su <li> correspondiente

# En total_data puedo guardar la info como me vaya sirviendo
total_data = [data_graf1] + [data_graf2] + [data_graf3]

print(total_data, file=utf8stdout)
