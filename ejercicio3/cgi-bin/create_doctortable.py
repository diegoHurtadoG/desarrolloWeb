#!/usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector

db = mysql.connector.connect(
    host="localhost",  # 127.0.0.1
    user="root",
    password="admin",
    database="ejercicio3"
)

cursor = db.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS ejercicio3.medico (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  experiencia VARCHAR (1000) NOT NULL,
  especialidad VARCHAR(20) NOT NULL,
  email VARCHAR(100) NULL,
  celular VARCHAR(100) NULL,
  foto INT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB DEFAULT CHARSET=utf8;
'''
               )

cursor.execute('''
CREATE TABLE IF NOT EXISTS ejercicio3.archivos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(256) NOT NULL,
  path VARCHAR (60) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB DEFAULT CHARSET=utf8;
'''
               )
print("Las tablas se crearon con éxito!")
