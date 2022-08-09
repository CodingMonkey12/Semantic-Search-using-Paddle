from fastapi import APIRouter
from models.Text import Text
import time
from pymilvus import connections, Collection
import pymysql
import requests

router = APIRouter(
    prefix='/search',
    tags=['中英文专利摘要查询'],
)

milvus_address = '192.168.96.101'
connections.connect(host=milvus_address, port='19530')

collection = Collection("multilingual")
collection.load()


# connect database
mysql_address = '192.168.96.102'
conn = pymysql.connect(
    host=mysql_address,
    user='root',
    password='123456',
    database='ipc_search',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()


@router.post("/")
def search(text: Text):
    if not text.data:
        return {'result': '请输入文本'}
    
    start_time = time.time()
    
    # get embeddings
    res = requests.post('http://localhost:1234/sen-to-vec/', json={'data': text.data}).json()

    print(time.time() - start_time)

    search_params = {"metric_type": "L2", "params": {"nprobe": 32}}

    milvus_results = collection.search(
        data=[res['result']], 
        anns_field="embeddings", 
        param=search_params, 
        limit=1000, 
        expr=None,
        consistency_level="Strong"
    )

    print(time.time() - start_time)

    results = []
    for result in milvus_results[0]:
        sql = f"""
        SELECT *
        FROM multilingual
        WHERE publication_number_sear='{result.id}'
        """
        try:
            cursor.execute(sql)
            results.append(cursor.fetchone())
        except Exception as e:
            print(e)
            continue
    
    print(time.time() - start_time)

    return {'result': results}
