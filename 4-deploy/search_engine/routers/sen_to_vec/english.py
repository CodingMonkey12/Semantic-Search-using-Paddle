from fastapi import APIRouter
from models.Text import Text
import paddle.inference as paddle_infer
import json
import paddlenlp as ppnlp
from paddlenlp.data import Tuple, Pad

router = APIRouter(
    prefix='/sen-to-vec/english',
    tags=['英文专利摘要向量化']
)

