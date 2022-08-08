from tqdm import tqdm
import pandas as pd
import requests
from pymilvus import connections, Collection
import pymysql
from pymysql.converters import escape_string

TABLE_NAME = 'multilingual'

# 1. connect milvus
milvus_address = '192.168.96.101'
connections.connect(host=milvus_address, port='19530')
collection = Collection(TABLE_NAME)

# 2. connect mysql
mysql_address = '192.168.96.102'
conn = pymysql.connect(
    host=mysql_address,
    user='root',
    password='123456',
    database='ipc_search'
)
cursor = conn.cursor()


# 3. load data
path = 'data/multilingual/'
data = pd.read_csv(path + 'data.csv', sep='\t')

for idx in tqdm(range(len(data['abstract_ab']))):
    try:
        # get embeddings
        res = requests.post('http://192.168.1.241:1234/sen-to-vec/', json={'data': data['abstract_ab'][idx]}).json()

        collection.insert([
            [data['publication_number_sear'][idx]],
            [res['result']]
        ])

        sql = f"""
        INSERT INTO {TABLE_NAME} (publication_number_sear, title, abstract_ab, ipc_main_stat)
        VALUES ('{data['publication_number_sear'][idx]}', '{data['title'][idx]}', '{escape_string(data['abstract_ab'][idx])}', '{data['ipc_main_stat'][idx]}')
        """
        cursor.execute(sql)

    except Exception as e:
        print(e)
        continue

conn.commit()
cursor.close()
conn.close()
