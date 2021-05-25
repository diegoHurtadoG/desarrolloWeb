#!/u/a/2019/descobar/public_anakena/venv/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector


class ManageDB:
    def __init__(self, host, user, password, db=None):
        self.__host = host
        self.__db = db
        self.__user = user
        self.__password = password

    def set_db(self, db):
        self.__db = db

    def __connect(self):
        credentials = {
            "host": self.__host,
            "user": self.__user,
            "password": self.__password
        }
        if self.__db:
            credentials["db"] = self.__db
        return mysql.connector.connect(**credentials)

    def perform_table_creation(self, path, multi=False):
        conn = self.__connect()
        cursor = conn.cursor()

        fp = open(path)
        sql = fp.read()
        result = cursor.execute(sql, multi=multi)
        if multi:
            result.send(None)
        fp.close()
        cursor.close()
        conn.close()

    def execute_query(self, query, multi=False):
        conn = self.__connect()
        cursor = conn.cursor()
        result = cursor.execute(query, multi=multi)
        if multi:
            result.send(None)
        queryset = cursor.fetchall()
        cursor.close()
        conn.close()
        return queryset

    def insert_sql_file(self, path):
        conn = self.__connect()
        cursor = conn.cursor()
        fp = open(path)
        queries = fp.readlines()
        fp.close()
        queries = [q.replace('\n', '') for q in queries]
        statement = ' '.join(queries)
        [_ for _ in conn.cmd_query_iter(statement)]
        conn.commit()
        cursor.close()
        conn.close()
