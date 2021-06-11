#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector


class ManageDB:
    def __init__(self, host, user, password, db=None):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db

    def set_db(self, db):
        self.__db = db

    def __connect(self):
        data = {
            'host': self.__host,
            'user': self.__user,
            'password': self.__password
        }
        if self.__db:
            data.update({'db': self.__db})
        return mysql.connector.connect(**data)

    def __make_query(self, query, multi=False):
        conn = self.__connect()
        cursor = conn.cursor()
        result = cursor.execute(query, multi=multi)
        if multi:
            result.send(None)
        queryset = cursor.fetchall()
        cursor.close()
        conn.close()
        return queryset

    @staticmethod
    def parse_queryset_to_dict(queryset, fields):
        parsed = [dict() for _ in range(len(queryset))]
        for i in range(len(queryset)):
            for j in range(len(fields)):
                parsed[i][fields[j]] = queryset[i][j]
        return parsed

    def perform_db_creation(self, path):
        db = self.__connect()
        cursor = db.cursor()
        fp = open(path)
        sql = fp.read()
        result = cursor.execute(sql, multi=True)
        result.send(None)
        fp.close()
        cursor.close()
        db.close()

    def insert_doctor(self, cellphone, email, speciality, experience, name, photo_id):
        db = self.__connect()
        cursor = db.cursor()
        query = """
            INSERT INTO medico (celular, email, especialidad, experiencia, nombre, photo_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (cellphone, email, speciality, experience, name, photo_id))
        db.commit()
        cursor.close()
        db.close()

    def insert_photo(self, name, path):
        db = self.__connect()
        cursor = db.cursor()
        query = """
            INSERT INTO archivo (name, path)
            VALUES (%s, %s)
        """
        cursor.execute(query, (name, path))
        db.commit()
        cursor.close()
        db.close()
        sql = """
            SELECT COUNT(id) FROM archivo;
        """
        counter = self.__make_query(sql)[0][0]
        return counter

    def get_doctors(self):
        sql = r"""
            SELECT ME.id, ME.nombre, ME.experiencia, ME.especialidad, ME.email, ME.celular, AR.name, AR.path
            FROM medico ME, archivo AR
            WHERE ME.photo_id = AR.id
        """
        qs = self.__make_query(sql)
        fields_name = ['id', 'name', 'experience', 'speciality', 'email', 'cellphone', 'photo_name', 'photo_path']
        doctors = self.parse_queryset_to_dict(qs, fields_name)
        return doctors

    def count_doctors(self):
        sql = """
            SELECT COUNT(id) FROM medico;
        """
        counter = self.__make_query(sql)[0][0]
        return counter
