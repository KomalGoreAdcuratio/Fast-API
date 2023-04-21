from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.get("/",description="Hi !!! It's get methods")
async def fun():
    return {"name":'komal', "age":23}    # ===> return dic         

@app.post("/")
async def fun():
    return {"Hello":"From Post FAst-API"}

@app.post("/{id}")
async def fun(id):
    return {"Hello":f"From Post FAst-API {id}"}


#### Query Parameter 

@app.get("/data")
async def fun(q = None):
    return {"Data from query": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool 

@app.put("/data/items}")
def update_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
