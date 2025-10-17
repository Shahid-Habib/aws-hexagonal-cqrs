# src/handlers/command_handler.py
from src.domain.product_service import ProductService
from src.adapters.dynamodb_adapter import DynamoDBAdapter

# Initialize domain service and adapter
product_service = ProductService()
dynamodb_adapter = DynamoDBAdapter()

def create_product_command(product):
    # Save product in the domain service
    product_service.create_product(product)
    # Also save product in the mock DynamoDB
    dynamodb_adapter.save_product(product)
    return product
