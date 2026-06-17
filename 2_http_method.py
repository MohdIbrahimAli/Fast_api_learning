from fastapi import FastAPI, Request
from mockdata import products
from dtos import ProductsDTO

app = FastAPI()

@app.get("/")
def root_():
    return "Welcome to learning Fastapi"

@app.get("/products")
def Products():
    return products

@app.get("/products/{prod}")
def Product_search(prod:int):
    for product in products:
        if prod == product.get("id"):
            return product
    else:
        return {"error": "Product not found for the ID"}

@app.post("/create_product/")
def create_product(data:ProductsDTO):
    data = data.model_dump()
    products.append(data)
    print(data)
    return {"Success":"Product created successfully", "data":products}

@app.put("/update_product/{prod_id}")
def update_product(data:ProductsDTO, prod_id:int):
    for index, product in enumerate(products):
        if product.get('id') == prod_id:
            products[index] = data.model_dump()
            return {"Success": "Product Updated successfully", "product":data}
        return{"error":"Product not found for the ID"}

@app.delete("/delete_product/{prod_id}")
def delete_product(prod_id:int):
    for product in products:
        if product.get("id") == prod_id:
            products.remove(product)
            return {"Success":"Product Deleted"}
            