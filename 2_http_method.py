from fastapi import FastAPI, Request
from mockdata import products
from dtos import ProductsDTO

app = FastAPI()

@app.get("/")  #Root path for the API
def root_():
    return "Welcome to learning Fastapi"

@app.get("/products")
def Products():
    return products  #returning all the products

@app.get("/products/{product_id}")
def Product_search(product_id:int):
    for product in products:
        if product_id == product.get("id"):   #information about a single product with their ID
            return product
    else:
        return {"error": "Product not found for the ID"}

@app.post("/create_product/")
def create_product(body:ProductsDTO):
    body = body.model_dump()  #using miodel.dump() to convert the pydantic object to a usable dict
    products.append(body)
    print(body)
    return {"Success":"Product created successfully", "body":products}

@app.put("/update_product/{prod_id}")
def update_product(body:ProductsDTO, prod_id:int):
    for index, product in enumerate(products):  #Enumerate gives us 2 values 1-index of value, 2-actual value
        if product.get('id') == prod_id:
            products[index] = body.model_dump()
            return {"Success": "Product Updated successfully", "product":body}
        return{"error":"Product not found for the ID"}

@app.delete("/delete_product/{prod_id}")
def delete_product(prod_id:int):
    for product in products:
        if product.get("id") == prod_id:
            products.remove(product)
            return {"Success":"Product Deleted successfully"}
        return{
            "error":"Product not found for the ID"
        }
            