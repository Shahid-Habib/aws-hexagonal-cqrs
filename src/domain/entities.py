# src/domain/entities.py
from datetime import datetime

class Product:
    def __init__(self, product_id: str, name: str, price: float, description: str, created_at: datetime):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.created_at = created_at

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price}, description='{self.description}', created_at={self.created_at})"
