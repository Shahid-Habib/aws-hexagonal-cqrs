# src/adapters/dynamodb_adapter.py

class DynamoDBAdapter:
    def __init__(self):
        # This will act like a fake DynamoDB table
        self.storage = {}

    def save_product(self, product):
        self.storage[product.product_id] = product
        print(f"Saved product to DynamoDB: {product}")

    def get_product(self, product_id):
        return self.storage.get(product_id)
