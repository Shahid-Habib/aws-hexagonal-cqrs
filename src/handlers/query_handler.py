# src/handlers/query_handler.py
from src.adapters.dynamodb_adapter import DynamoDBAdapter

# Initialize adapter (same as command handler)
dynamodb_adapter = DynamoDBAdapter()

def get_product_query(product_id):
    return dynamodb_adapter.get_product(product_id)
