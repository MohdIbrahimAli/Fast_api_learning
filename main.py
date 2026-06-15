from fastapi import FastAPI, Request
from mockdata import products

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the ecommerce world"

#Path parameters
@app.get("/product/{prod_id}")
def product_get(prod_id:int):
    for product in products:
        if product.get("id") == prod_id:
            return product
    return {
        "error": "Product not found"
    }

#Query parameters
@app.get("/greet")
def greeting(name:str, age:int=12):
    return {
        "greeting":f"Hello {name} how are you",
        "age":f"Your age is {age}"
    }

#Requests
@app.get("/search")
def search(request:Request):
    queary_params = dict(request.query_params)
    return {
        "msg":f"hello {queary_params.get("name")}! your age is {queary_params.get("age")}"
    }