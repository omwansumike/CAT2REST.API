from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" for products
products = []

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    # Validate input
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400  # Bad Request

    # Create a new product
    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'description': data.get('description', ''),  # Optional
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201  # Created

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200  # OK

if __name__ == '__main__':
    app.run(debug=True)

