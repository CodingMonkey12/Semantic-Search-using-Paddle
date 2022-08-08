from fastapi import FastAPI
import uvicorn
from routers import sen_to_vec, search
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI()

# app.include_router(sen_to_vec.chinese.router)
# app.include_router(sen_to_vec.english.router)
app.include_router(sen_to_vec.multilingual.router)
# app.include_router(search.chinese.router)
# app.include_router(search.english.router)


@app.get('/', tags=['首页'])
def index():
    return {'msg': '进入 /docs 查看文档'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=1234, reload=True, debug=True)
