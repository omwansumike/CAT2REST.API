
import requests

BASE_URL = "http://127.0.0.1:5000/products"

# Add a new product
def add_product():
    product_data = {
        "name": "Phone",
        "description": "A smartphone with a great camera",
        "price": 699.99
    }
    response = requests.post(BASE_URL, json=product_data)
    print("POST Response:", response.status_code, response.json())

# Retrieve all products
def get_products():
    response = requests.get(BASE_URL)
    print("GET Response:", response.status_code, response.json())

if __name__ == "__main__":
    add_product()
    get_products()
