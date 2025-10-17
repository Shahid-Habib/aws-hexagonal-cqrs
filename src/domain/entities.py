from datetime import datetime

class Product:
    def __init__(self, product_id, name, price, description=None, created_at=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.created_at = created_at or datetime.utcnow()

    def __repr__(self):
        return (f"Product(id={self.product_id}, name='{self.name}', "
                f"price={self.price}, description='{self.description}', created_at={self.created_at})")
