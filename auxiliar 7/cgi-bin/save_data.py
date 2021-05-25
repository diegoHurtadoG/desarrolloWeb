#!/opt/homebrew/opt/python@3.8/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector
import hashlib
from utils import imprimeerror
import os
import filetype

MAX_FILE_SIZE = 10000 * 1000  # 10 MB


class HackBoxDatabase:

    def __init__(self, user, password):
        self.db = mysql.connector.connect(
            host='localhost',
            user=user,
            password=password,
            database='hackbox'
        )
        self.cursor = self.db.cursor()

    def save_data(self, data):
        # procesar y guardar el archivo
        fileobj = data[3]
        filename = fileobj.filename

        if not filename:
            imprimeerror(10, 'Archivo no subido')

        # verificamos el tipo
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            imprimeerror(1000, 'Tamaño excede 10mb')

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM archivos"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = 'media/' + hash_archivo
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if tipo.mime != 'application/pdf':
            os.remove(file_path)
            imprimeerror(40, 'Tipo archivo no es pdf')

        # guardamos la imagen en la db
        sql = """
            INSERT INTO archivos (nombre, path)
            VALUES (%s, %s)
        """
        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id
        id_archivo = self.cursor.getlastrowid()

        # guardamos el comentario en la db
        sql = """
            INSERT INTO usuario (nombre, edad, comentario, archivo, ......) 
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(sql, (*data[0:3], id_archivo))  # ejecuto la consulta
        self.db.commit()  # modifico la base de datos

    def get_all(self, tablename):
        sql = f"""
            SELECT * FROM {tablename} ORDER BY `id` DESC
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data
