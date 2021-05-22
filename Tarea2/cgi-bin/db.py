#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import os
import filetype

MAX_FILE_SIZE = 1000 * 1000 * 10  # b -> kb -> mb -> 10mb


class Avistamiento:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
        '''
    data = (
    form['region'].value, form['comuna'].value, form['sector'].value,
    form['nombre'].value, form['email'].value, form['celular'],
    form['dia-hora-avistamiento'], form['tipo-avistamiento'], form['estado-avistamiento'], form['fotos-avistamiento']
)
        '''

    def save_avistamiento(self, data):
        ############ VALIDACIONES INPUTS FACILES ##############
        region = data[0]
        comuna = data[1]
        sector = data[2]
        nombre = data[3]
        email = data[4]
        celular = data[5]

        if region == "":  # Se tendra que validar tambien que la region existe en la bdd
            print("Region mal")
            # No se si printear o hacer algun log en algun lado

        if comuna == "":
            print("Comuna mal")
            # Lo mismo que en region

        if sector != "" and len(sector) > 100:
            print("Sector muy largo")

        if nombre == "" or len(nombre) > 200:
            print("Nombre no existe o es muy largo")

        if email == "":  # Validar con regex aqui
            print("Email no existe o no cumple formato")

        if celular != "" and False:  # Validar con regex aqui
            print("Celular no cumple formato")

        # Horario, tipo, estado y fotos los hago despues por que son los que se pueden extender

        ############ VALIDACIONES FOTOS ##############
        fileobj = data[9]  # Este problema es el mismo que voy a tener despues con que es solo 1 foto de 1 avistamiento
        filename = fileobj.filename

        if not filename:
            print("El archivo no se subio correctamente")

        # Veamos que no sea mas grande de lo aceptado
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            print("El archivo supera lo aceptado (igual se subio)")

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM fotos"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso || ESTA LINEA ME PUEDE SERVIR PARA COMUNAS Y REGIONES
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'cgi-bin/Fotos/Avistamientos' + hash_archivo + ".jpg"
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if tipo.mime != 'image/jpeg':
            os.remove(file_path)
            print("El archivo se elimino por ser un tipo no valido")

        sql = '''
                    INSERT INTO medico (nombre, experiencia, especialidad, email, celular, foto) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
        self.cursor.execute(sql, data)  # ejecuto la consulta
        self.db.commit()  # obtengo id

        id_avistamiento = self.cursor.lastrowid

        # guardamos la imagen en la db
        # Mismo problema con cantidad de fotos
        sql = """
                    INSERT INTO foto (path, nombre, id_avistamiento)
                    VALUES (%s, %s,%s)
                """

        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id

        # En la consulta de aqui abajo, las ultimas dos son total avistamientos y total fotos, pero puse los id para testear
    def get_lista_avistamientos(self):
        sql = f"""
                    SELECT avistamiento.id, avistamiento.dia_hora, comuna.nombre, avistamiento.sector, avistamiento.nombre, avistamiento.id, avistamiento.id
                    FROM avistamiento
                    INNER JOIN comuna ON comuna.id = avistamiento.comuna_id
                """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data

    def get_lista_portada(self):
        sql = f"""
                            SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo 
                            FROM avistamiento AV, detalle_avistamiento DA, comuna CO 
                            WHERE DA.avistamiento_id = AV.id 
                            AND AV.comuna_id=CO.id 
                            ORDER BY DA.dia_hora DESC LIMIT 5
                        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data