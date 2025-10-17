from datetime import datetime
from src.domain.entities import Product
from src.domain.product_service import ProductService

# Create a product
product = Product(
    product_id="1",
    name="Laptop",
    price=1500,
    description="Gaming laptop",
    created_at=datetime.utcnow()
)

# Create a service and add the product
service = ProductService()
service.create_product(product)

# Retrieve product
retrieved = service.get_product("1")
print(retrieved)
