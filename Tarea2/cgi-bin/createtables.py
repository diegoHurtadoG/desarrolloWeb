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


db_creator = CreateDB('127.0.0.1', 'root', "admin", "tarea2")
db_creator.perform_creation('../sql/total.sql')
