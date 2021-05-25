#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector


class CreateDB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def perform_creation(self, path):
        fp = open(path)
        sql = fp.read()
        result = self.cursor.execute(sql, multi=True)
        result.send(None)
        fp.close()

    def create_insert(self, path): #Este funciona para crear las tablas y agregar regiones y comunas
        with open(path, 'r') as sql_file:
            result_iterator = self.cursor.execute(sql_file.read(), multi=True)
            for res in result_iterator:
                print("Running query: ", res)  # Will print out a short representation of the query
                print(f"Affected {res.rowcount} rows")

            self.db.commit()  # Remember to commit all your changes!

    def insert_queries(self,path):
        self.cursor = self.db.cursor()
        fp = open(path)
        queries = fp.readlines()
        fp.close()
        queries = [q.replace('\n', '') for q in queries]
        try:
            for q in queries:
                self.cursor.execute(q)

            self.db.commit()
        except:
            self.db.rollback()
        self.cursor.close()
        print("Datos ingresados")


db_creator = CreateDB('127.0.0.1', 'root', "admin", "tarea2")


db_creator.create_insert('../sql/total.sql')
# db_creator.perform_creation('../sql/total.sql')
# db_creator.perform_creation('../sql/tarea2.sql')
# db_creator.insert_queries('../sql/region-comuna.sql')
print("Listo!")