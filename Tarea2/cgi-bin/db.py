#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import os
import filetype
import time

MAX_FILE_SIZE = 1000 * 1000 * 10  # b -> kb -> mb -> 10mb


def string_validator(s, min, max, base=''):
    if type(s) == str and s != base and min <= len(s) <= max:
        return True
    else:
        return False


def ajustar_tamano(s, size=2):
    while len(s) < size:
        s = '0' + s
    return s


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
        error_list = []

        ############ VALIDACIONES INPUTS FACILES ##############
        region = data[0]
        comuna = data[1]
        sector = data[2]
        nombre = data[3]
        email = data[4]
        celular = data[5]

        if region == "sin-region":  # Se tendra que validar tambien que la region existe en la bdd
            error_list.append('La region no es valida')

        if comuna == "sin-comuna":
            error_list.append('La comuna no es valida')

        # Vamos a obtener altiro el id comuna
        sql = '''
                    SELECT id FROM comuna
                    WHERE nombre LIKE %s
        '''

        self.cursor.execute(sql, ('%' + comuna + '%',))
        id_comuna = self.cursor.fetchall()[0][0]  # fetchall() retorna una lista de tuplas con las rows de la consulta

        if sector != "" and len(sector) > 100:
            error_list.append('El sector supera cantidad de caracteres')

        if nombre == "" or len(nombre) > 200:
            error_list.append('Nombre no existe o es muy largo')

        if email == "":  # Validar con regex aqui
            error_list.append('Email no existe o no cumple con formato')

        if celular != "" and False:  # Validar con regex aqui, quiza cuando no se envia dato, el valor default no es ""
            error_list.append('Celular no cumple formato')

        sql = '''
                    INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''

        # En la tabla avistamiento, va la fecha en que se sube a la bdd, en detalle avistamiento va la fecha del detalle
        fecha_ahora_formato = time.strftime('%Y-%m-%d %H:%M')

        self.cursor.execute(sql,
                            (id_comuna, fecha_ahora_formato, sector, nombre, email, celular))  # ejecuto la consulta
        self.db.commit()  # obtengo id

        id_avistamiento = self.cursor.lastrowid

        # Horario, tipo, estado y fotos se trabajan como listas, pues son los que se pueden agregar

        id_detalles = []

        horario_list = data[6]
        tipo_list = data[7]
        estado_list = data[8]

        for idx, h in enumerate(horario_list):
            if h == '':
                error_list.append('El horario numero ' + str(idx) + ' no es valido o no puede ser vacio.')

        for idx, t in enumerate(tipo_list):
            if t == '':
                error_list.append('El tipo numero ' + str(idx) + ' no es valido o no puede ser vacio.')

        for idx, e in enumerate(estado_list):
            if e == '':
                error_list.append('El estado numero ' + str(idx) + ' no es valido o no puede ser vacio.')

        # Voy a abusar de que las 3 listas tienen el mismo largo
        for i in range(len(horario_list)):
            sql = '''
                        INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) 
                        VALUES (%s, %s, %s, %s)
                            '''
            self.cursor.execute(sql,
                                (horario_list[i], tipo_list[i], estado_list[i], id_avistamiento))  # ejecuto la consulta
            self.db.commit()  # obtengo id

            id_detalles.append(self.cursor.lastrowid)

        ####################### EN TEORIA, de aqui para arriba:
        # Ya tengo la info validada (menos fotos)
        # Ya tengo agregado a tabla avistamiento
        # Ya tengo agregado a detalle_avistamiento
        # Los ids de cada detalle los guarde en id_detalles

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
        sql = "SELECT COUNT(id) FROM foto"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso || ESTA LINEA ME PUEDE SERVIR PARA COMUNAS Y REGIONES
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = './Fotos/Avistamientos/' + hash_archivo + ".jpg"
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if tipo.mime != 'image/jpeg':
            os.remove(file_path)
            print("El archivo se elimino por ser un tipo no valido")

        sql = '''
                    INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id) 
                    VALUES (%s, %s, %s)
                '''
        self.cursor.execute(sql, (file_path, filename, id_detalles[0]))
        # El id_detalles[0] lo hice para test, pero deberia ir insertando cada foto con su detalle
        self.db.commit()  # obtengo id


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
