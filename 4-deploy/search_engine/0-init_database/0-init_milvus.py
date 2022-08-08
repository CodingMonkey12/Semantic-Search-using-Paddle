from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType

# 1. milvus host ip, it will be changed every time when restart the docker
milvus_address = '192.168.96.101'
connections.connect(host=milvus_address, port='19530')

# 2. create the collection
TABLE_NAME = 'multilingual'

ipc_main_stat = FieldSchema(name='publication_number_sear', dtype=DataType.VARCHAR, is_primary=True, max_length=255)
embeddings = FieldSchema(name='embeddings', dtype=DataType.FLOAT_VECTOR, dim=256)

schema = CollectionSchema(
    fields = [ipc_main_stat, embeddings],
    description = 'multilingual'
)

collection = Collection(name=TABLE_NAME, schema=schema)

# 3. set an index
index_param = {
    'metric_type': 'L2',
    'index_type': 'IVF_SQ8',
    'params': {'nlist': 512} 
}
collection.create_index('embeddings', index_param)

print('init milvus')
