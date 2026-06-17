from pydantic import BaseModel

class ProductsDTO(BaseModel):
    id:int
    brand:str
    price:int
    name:str

