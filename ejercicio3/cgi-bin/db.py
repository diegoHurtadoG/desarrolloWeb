#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import os
import filetype

MAX_FILE_SIZE = 1000 * 1000 * 10  # b -> kb -> mb -> 10mb


class Doctor:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_doctor(self, data):
        fileobj = data[5]
        filename = fileobj.filename

        if not filename:
            print("El archivo no se subio correctamente")

        # Veamos que no sea mas grande de lo aceptado
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            print("El archivo supera lo aceptado (igual se subio)")

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM archivos"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'cgi-bin/media/' + hash_archivo +".jpg"
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if tipo.mime != 'image/jpeg':
            os.remove(file_path)
            print("El archivo se elimino por ser un tipo no valido")

        # guardamos la imagen en la db
        sql = """
            INSERT INTO archivos (nombre, path)
            VALUES (%s, %s)
        """

        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id
        id_archivo = self.cursor.lastrowid

        sql = '''
                    INSERT INTO medico (nombre, experiencia, especialidad, email, celular, foto) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
        self.cursor.execute(sql, (*data[0:5], id_archivo))  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

    def get_doctors(self):
        sql = f"""
                    SELECT medico.id, medico.nombre, medico.experiencia, medico.especialidad, medico.email, medico.celular, archivos.path
                    FROM medico
                    INNER JOIN archivos ON medico.foto=archivos.id;
                """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data
