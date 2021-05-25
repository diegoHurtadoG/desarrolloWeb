#!/u/a/2019/descobar/public_anakena/venv/bin/python3
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

load_dotenv()

DB_TABLE_NAME = os.getenv('db_table_name')
DB_USERNAME = os.getenv('db_username')
DB_PASSWORD = os.getenv('db_password')
DB_HOST = os.getenv('db_host')
