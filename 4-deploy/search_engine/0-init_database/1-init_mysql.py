import pymysql


# connect to mysql
mysql_address = '192.168.96.102'
conn = pymysql.connect(
    host=mysql_address,
    user='root',
    password='123456'
)
cursor = conn.cursor()

# create database
try:
    cursor.execute('CREATE DATABASE ipc_search')
except Exception as e:
    print(e)

# connect database
conn = pymysql.connect(
    host=mysql_address,
    user='root',
    password='123456',
    database='ipc_search'
)
cursor = conn.cursor()

# create table
TABLE_NAME = 'multilingual'
cursor.execute(
    f"""
    CREATE TABLE {TABLE_NAME}(
        publication_number_sear varchar(255) PRIMARY KEY,
        title varchar(255),
        abstract_ab text,
        ipc_main_stat varchar(255)
        )
    """
    )

print('init mysql')
