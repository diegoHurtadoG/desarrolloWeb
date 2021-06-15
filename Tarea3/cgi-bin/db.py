#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import os
import filetype
import time
import re
import json

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
        form['nombre'].value, form['email'].value, form['celular'].value,
        form.getlist('dia-hora-avistamiento'), form.getlist('tipo-avistamiento'), form.getlist('estado-avistamiento'),
        form['fotos-avistamiento'], # Ver bien si los archivos los llamo con getlist o con form[''], sin el .value (o con, revisar ejercicio)
        form.getlist('cantidad-fotos-avistamiento')
    )
        '''

    # Tengo el numero de foto que estoy validando
    # Tengo una lista con la cantidad de fotos por avistamiento
    def indexar_foto(self, num, lista):
        for idx, e in enumerate(lista):
            if num - int(e) <= 0:
                return idx
            else:
                num -= int(e)
        return 0  # No deberia llegar aqui nunca

    def last_insert_id(self):
        sql = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def save_avistamiento(self, data):
        error_list = []
        regexEmail = '^(([^<>()[\]\., ;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$'
        regexCelular = '^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$'
        try:

            ############ VALIDACIONES INPUTS FACILES ##############
            region = data[0]
            comuna = data[1]
            sector = data[2]
            nombre = data[3]
            email = data[4]
            celular = data[5]

            # Esta consulta valida que region este en la bdd
            sql = '''
                        SELECT count(id) FROM region
                        WHERE nombre LIKE %s
                    '''
            self.cursor.execute(sql, ('%' + region + '%',))
            buff = self.cursor.fetchall()[0][0]
            if region == "sin-region" or buff != 1:  # Se tendra que validar tambien que la region existe en la bdd
                error_list.append('La region no es valida')

            # Esta consulta valida que comuna este en la bdd
            sql = '''
                        SELECT count(id) FROM comuna
                        WHERE nombre LIKE %s
                            '''
            self.cursor.execute(sql, ('%' + comuna + '%',))
            buff = self.cursor.fetchall()[0][0]
            if comuna == "sin-comuna" or buff != 1:
                error_list.append('La comuna no es valida')

            # Vamos a obtener altiro el id comuna
            sql = '''
                        SELECT id FROM comuna
                        WHERE nombre LIKE %s
            '''

            self.cursor.execute(sql, ('%' + comuna + '%',))
            id_comuna = self.cursor.fetchall()[0][
                0]  # fetchall() retorna una lista de tuplas con las rows de la consulta

            if sector != "" and len(sector) > 100:
                error_list.append('El sector supera cantidad de caracteres')

            if nombre == "" or len(nombre) > 200:
                error_list.append('Nombre no existe o es muy largo')

            if email == "" or not re.search(regexEmail, email):  # Validar con regex aqui
                error_list.append('Email no existe o no cumple con formato')

            if celular != "" and not re.search(regexCelular,
                                               celular):  # Validar con regex aqui, quiza cuando no se envia dato, el valor default no es ""
                error_list.append('Celular no cumple formato')

            sql = '''
                        INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                    '''

            # En la tabla avistamiento, va la fecha en que se sube a la bdd, en detalle avistamiento va la fecha del detalle
            fecha_ahora_formato = time.strftime('%Y-%m-%d %H:%M')

            self.cursor.execute(sql,
                                (id_comuna, fecha_ahora_formato, sector, nombre, email, celular))  # ejecuto la consulta

            id_avistamiento = self.last_insert_id()

            ############# VALIDACION CON LISTAS
            ############# Horario, tipo, estado y fotos se trabajan como listas, pues son los que se pueden agregar
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

            print(tipo_list)
            # Voy a abusar de que las 3 listas tienen el mismo largo
            for i in range(len(horario_list)):
                sql = '''
                            INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id) 
                            VALUES (%s, %s, %s, %s)
                                '''
                self.cursor.execute(sql,
                                    (horario_list[i], tipo_list[i], estado_list[i],
                                     id_avistamiento))  # ejecuto la consulta
                id_detalles.append(self.last_insert_id())

            ####################### EN TEORIA, de aqui para arriba:
            # Ya tengo la info validada (menos fotos)
            # Ya tengo agregado a tabla avistamiento
            # Ya tengo agregado a detalle_avistamiento
            # Los ids de cada detalle los guarde en id_detalles

            ############ VALIDACIONES FOTOS ##############
            cantidad_fotos_avistamiento = data[
                10]  # Esto tiene una lista de ints con cuantos avistamientos tiene cada av

            fileobj_list = data[9]
            if type(fileobj_list) != list:
                fileobj_list = [fileobj_list]

            numero_foto = 1
            for fileobj in fileobj_list:
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
                total = self.cursor.fetchall()[0][
                            0] + 1  # peligroso || ESTA LINEA ME PUEDE SERVIR PARA COMUNAS Y REGIONES
                hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

                # guardar el archivo
                file_path = './Fotos/Avistamientos/' + hash_archivo + ".jpg"
                open(file_path, 'wb').write(fileobj.file.read())

                # verificamos el tipo, si no es valido lo borramos de la db
                tipo = filetype.guess(file_path)
                if not re.search("^image/", tipo.mime):
                    os.remove(file_path)
                    print("El archivo se elimino por ser un tipo no valido")

                sql = '''
                            INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id) 
                            VALUES (%s, %s, %s)
                        '''
                self.cursor.execute(sql, (
                    file_path, hash_archivo + '.jpg',
                    id_detalles[self.indexar_foto(numero_foto, cantidad_fotos_avistamiento)]))
                numero_foto += 1

            ####################### EN TEORIA, de aqui para arriba:
            # Ya tengo la info validada (menos fotos)
            # Ya tengo agregado a tabla avistamiento
            # Ya tengo agregado a detalle_avistamiento
            # Los ids de cada detalle los guarde en id_detalles
            # Ya valide fotos multiples
            # Asocie cada foto con su id

            if len(error_list) > 0:
                print('Lista errores: ', error_list)
                self.db.rollback()  # Con esto saco los execute
                return error_list
            else:
                self.db.commit()
                print("Subido sin errores")
                return True
        except:
            for error in error_list:
                print("<li>" + error + '</li>')
            print(
                '<li> Revisar las fotos (Minimo 1 por avistamiento y algun formato de imagen), no necesariamente estan mal </li>')

    def get_lista_avistamientos(self):
        sql = f"""
                    SELECT avistamiento.id, avistamiento.dia_hora, comuna.nombre, avistamiento.sector, avistamiento.nombre
                    FROM avistamiento
                    INNER JOIN comuna ON comuna.id = avistamiento.comuna_id
                """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()  # retornamos la data

        return data

    # No esta funcionando
    def get_total_avistamientos(self, id_av):
        sql = f"""
                    SELECT count(id) FROM detalle_avistamiento
                    WHERE avistamiento_id = %s
                        """
        self.cursor.execute(sql, (id_av,))
        data = self.cursor.fetchall()[0][0]  # retornamos la data

        return data

    # Me falta conseguir alguna forma de obtener id_det
    def get_total_fotos(self, id_av):
        num_fotos = 0
        sql = f'''
                    SELECT id
                    FROM detalle_avistamiento
                    WHERE avistamiento_id = %s
                '''
        self.cursor.execute(sql, (id_av,))
        buff = self.cursor.fetchall()  # Deberia retornar una tupla con los id_detalle de cada detalle del avistamiento

        for b in buff:
            sql = f"""
                        SELECT count(id) FROM foto
                        WHERE detalle_avistamiento_id = %s
                        """
            self.cursor.execute(sql, (b[0],))
            num_fotos += self.cursor.fetchall()[0][0]  # retornamos la data

        return num_fotos

    def get_lista_portada(self):
        sql = f"""
                            SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo, DA.id
                            FROM avistamiento AV, detalle_avistamiento DA, comuna CO 
                            WHERE DA.avistamiento_id = AV.id 
                            AND AV.comuna_id=CO.id 
                            ORDER BY DA.dia_hora DESC LIMIT 5
                        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # retornamos la data

    def get_fotos_portada(self, id_det):
        sql = f"""
                            SELECT ruta_archivo
                            FROM foto
                            WHERE detalle_avistamiento_id = %s
                        """
        self.cursor.execute(sql, (id_det,))
        return self.cursor.fetchall()  # retornamos la data

    def get_info_av(self, id_av):
        sql = f"""
                            SELECT AV.nombre, AV.email, AV.celular, R.nombre, C.nombre, AV.sector, DA.tipo, DA.estado, DA.dia_hora, F.ruta_archivo
                            FROM avistamiento AV, detalle_avistamiento DA, foto F, comuna C, region R
                            WHERE AV.id = %s
                            AND AV.comuna_id = C.id
                            AND C.region_id = R.id
                            AND AV.id = DA.avistamiento_id
                            AND F.detalle_avistamiento_id = DA.id
                """
        self.cursor.execute(sql, (id_av,))
        data = self.cursor.fetchall()  # Tupla de la forma ( (av.nombre, av.email, ...,) ( av.nombre, av.email , ..., ))

        return data

    # Para grafico 1
    def get_cantidad_por_dia(self):
        sql = f"""
                            SELECT COUNT(*) AS cantidad, DATE_FORMAT(dia_hora,'%d-%c-%Y') as fecha
                            FROM detalle_avistamiento
                            GROUP BY DATE_FORMAT(dia_hora,'%d-%c-%Y')
                """
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()  # Retorna algo del tipo ((3, 2019-08-20), (1, 2020-01-27))
        json_str = json.dumps(data_tuple)  # Retorna un str -> '[[3, 2019-08-20], [1, 2020-01-27]]'
        json_arr = json.loads(json_str)  # Retorna un json_array -> [[3, 2019-08-20], [1, 2020-01-27]]
        return json_arr  # A este json_arr ya se le pueden aplicar json_arr[i][j]

    # Para grafico 2
    def get_cantidad_por_tipo(self):
        sql = f"""
                            SELECT COUNT(*) AS cantidad, tipo
                            FROM detalle_avistamiento
                            GROUP BY tipo
                """
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()  # Retorna algo del tipo ((3, arácnido), (1, insecto))
        json_str = json.dumps(data_tuple)  # Retorna un str -> '[[3, 'arácnido'], [1, 'insecto']]'
        json_arr = json.loads(json_str)  # Retorna un json_array -> [[3, 'arácnido'], [1, 'insecto']]
        return json_arr  # A este json_arr ya se le pueden aplicar json_arr[i][j]

    # Para grafico 3
    def get_cantidad_mensual_por_estado(self):
        sql = f"""
                            SELECT COUNT(*) AS cantidad, estado, DATE_FORMAT(dia_hora,'%c') as mes
                            FROM detalle_avistamiento
                            GROUP BY DATE_FORMAT(dia_hora,'%c'), estado
                    """
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()  # Retorna algo del tipo ((3, vivo, 4), (1, insecto, 8)), donde el ultimo es el numero del mes
        json_str = json.dumps(data_tuple)  # Retorna un str -> '[[3, vivo, 4], [1, insecto, 8]]'
        json_arr = json.loads(json_str)  # Retorna un json_array -> [[3, vivo, 4], [1, insecto, 8]]
        return json_arr  # A este json_arr ya se le pueden aplicar json_arr[i][j]

    # Para mapa
    def get_info_mapa(self):
        sql = f"""
                            SELECT comuna.nombre AS comuna, avistamiento.id AS av_id, detalle_avistamiento.id AS det_id, detalle_avistamiento.dia_hora, detalle_avistamiento.tipo, detalle_avistamiento.estado, foto.ruta_archivo AS path_foto
                            FROM (((avistamiento 
                                   INNER JOIN comuna ON avistamiento.comuna_id = comuna.id) 
                                  INNER JOIN detalle_avistamiento ON avistamiento.id = detalle_avistamiento.avistamiento_id)
                                  INNER JOIN foto ON detalle_avistamiento.id = foto.detalle_avistamiento_id)
                            ORDER BY detalle_avistamiento.id ASC
                    """
        self.cursor.execute(sql)
        data_tuple = self.cursor.fetchall()  # Retorna algo del tipo ((row1), (row2))
            # Las rows son (nombreComuna, id_av, id_detalle, dia_hora, tipo, estado, path_foto)
        json_str = json.dumps(data_tuple, default=str)  # Retorna un str -> '[[row1], [row2]]'  ####AQUI ESTA EL PROBLEMA QUE ME TIRA EL CMD
        json_arr = json.loads(json_str)  # Retorna un json_array -> [[row1], [row2]]
        return json_arr  # A este json_arr ya se le pueden aplicar json_arr[i][j]
