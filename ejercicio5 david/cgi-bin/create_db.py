#!/usr/bin/python3
# -*- coding: utf-8 -*-

from manage_db import ManageDB

db_creator = ManageDB('localhost', 'root', '')
db_creator.perform_db_creation('../db-ejercicio4.sql')
