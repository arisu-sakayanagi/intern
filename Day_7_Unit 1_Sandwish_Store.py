from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: str

data = {
    1: {
        "name": "a",
        "price": 100,
        "quantity": "normal"
    },
    2: {
        "name": "b",
        "price": 200,
        "quantity": "good"
    },
    3: {
        "name": "c",
        "price": 50,
        "quantity": "bad"
    },
    4: {
        "name": "d",
        "price": 300,
        "quantity": "good"
    }
}

@app.get('/', tags=["Item"])
def getItems():
    return data

@app.get('/{id}', tags=["Item"])
def getItems(id: int):
    if id in data:
        return data[id]
    else:
        return {"Error" : "Not found"}

@app.post('/{id}', tags=["Item"])
def addItems(id: int, item : Item):
    if id in data:
        return {"Error": "Exist!"}
    else:
        data[id] = item
    return data[id]

@app.put('/{id}', tags=["Item"])
def updateItem(id: int, item : Item):
    if id in data:
        data[id].update(item)
        return data[id]
    else:
        return {"Error" : "Not found"}

@app.delete('/{id}', tags=["Item"])
def deleteItem(id: int):
    if id in data:
        del data[id]
        return {"Deleted"}
    else:
        return {"Error" : "Not found"}
