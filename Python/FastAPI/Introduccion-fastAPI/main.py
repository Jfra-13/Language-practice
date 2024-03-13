from typing import Union
from fastapi import FastAPI, Query, Path
from models.product import Product
from routers.product import router as product_router

app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello': 'world'}


@app.get("/items/{item_id}/{q}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'User': q}

#--------------------------------------------------------------

app.include_router(product_router)



