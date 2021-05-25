#!/u/a/2019/descobar/public_anakena/venv/bin/python3
# -*- coding: utf-8 -*-

from deploy_db.connect_db import ManageDB
from deploy_db.env_vars import DB_HOST, DB_PASSWORD, DB_TABLE_NAME, DB_USERNAME


        
db_creator = ManageDB(DB_HOST, DB_USERNAME, DB_PASSWORD)
db_creator.perform_table_creation('./tarea2.sql', True)
db_creator.set_db(DB_TABLE_NAME)
db_creator.insert_sql_file('./region-comuna.sql')
