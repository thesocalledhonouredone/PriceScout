from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
from datetime import datetime

class Controller:
    def __init__(self):
        self.connection_string = os.environ.get("MONGODB_URI")
        self.client = MongoClient(self.connection_string)
        self.db = self.client["product-scanner"]
        self.products_collections = self.db["products"]

    def get_all_products(self):
        products = self.products_collections.find()
        result = []
        
        for p in products:
            result.append({
                "_id": str(p["_id"]),
                "product_name": p["product_name"],
                "createdAt": p["createdAt"],
                "lowest_price": p["lowest_price"],
                "lowest_price_link": p["lowest_price_link"]
            })
        return result
    
    def insert_new_product(self, new_product: str):
        already_inserted = self.products_collections.find_one({"product_name": new_product})
        if already_inserted is None:
            self.products_collections.insert_one({
                "product_name": new_product,
                "createdAt": datetime.now(),
                "lowest_price": None,
                "lowest_price_link": None
            })
