from fastapi import FastAPI
from db_contorller import Controller
from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    

app = FastAPI()
cont = Controller()

@app.get("/")
def home():
    return {
        "page": "Home"
    }
    
@app.get("/products")
def get_all_products():
    return cont.get_all_products()

@app.post("/products")
def insert_all_products(product: Product):
    product = dict(product)
    cont.insert_new_product(product['product_name'])