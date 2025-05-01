import os
from pathlib import Path
import pymysql
from dotenv import load_dotenv
import sys

load_dotenv(Path('.env'))
#Настройки подключения

dbconfig_read = {'host': os.environ.get("HOST_READ"),
                 'user': os.environ.get("USER_READ"),
                 'password': os.environ.get("PASSWORD_READ"),
                 'database': os.environ.get("DATA_BASE")}

dbconfig_write = {'host': os.environ.get("HOST_WRITE"),
                  'user': os.environ.get("USER_WRITE"),
                  'password': os.environ.get("PASSWORD_WRITE"),
                  'database': os.environ.get("DATA_BASE_WRITE")}

#Проверка на возможные ошибки
try:
    conn_read = pymysql.connect(**dbconfig_read)
    conn_write = pymysql.connect(**dbconfig_write)

    cursor_read = conn_read.cursor()
    cursor_write = conn_write.cursor()
    print("Connection successful!")
except pymysql.MySQLError as e:
    print(f"Ошибка подключения к базе данных \n{e}")
    sys.exit(1)


# Подключение к базам sakila и group_111124_fp_Vadym_Prudnikov
def conn_read():
    return pymysql.connect(**dbconfig_read)


def conn_write():
    return pymysql.connect(**dbconfig_write)


