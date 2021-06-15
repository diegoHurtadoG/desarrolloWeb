#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import db

hbdb = db.Avistamiento('127.0.0.1', 'root', "admin", "tarea2")

# print('Content-type: text/html\r\n\r\n')
print('Content-type: application/json\r\n\r\n')

# Aqui tengo que obtener la data para los graficos y guardarlas en variables, estilo
data_mapa = hbdb.get_info_mapa() # Las rows son (nombreComuna, id_av, id_detalle, dia_hora, tipo, estado, path_foto)


jfile = open("cgi-bin/chile_comunas.json")
comunas_dic = json.loads(jfile.read())  # Esto debiese retornar un diccionario
jfile.close()

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

for i in data_mapa:
    for j in comunas_dic:
        if i[0]==j["name"]:
            i.append(j["lng"])
            i.append(j["lat"])
            break

# En total_data puedo guardar la info como me vaya sirviendo
total_data = data_mapa

print(total_data, file=utf8stdout)
# total_data tiene:
# [0] nombre comuna
# [1] id Avistamiento
# [2] id Detalle
# [3] Fecha
# [4] Tipo
# [5] Estado
# [6] Foto (En caso de haber mas de una, se va a tener otra tupla)
# [7] Lng
# [8] Lat
