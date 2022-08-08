from fastapi import APIRouter
from models.Text import Text
import time

router = APIRouter(
    prefix='/search/english',
    tags=['英文专利摘要查询']
)
