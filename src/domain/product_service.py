# src/domain/product_service.py
from src.domain.entities import Product

class ProductService:
    def __init__(self):
        self.products = {}

    def create_product(self, product: Product):
        self.products[product.product_id] = product  # use product_id
        return product

    def get_product(self, product_id):
        return self.products.get(product_id)
