from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Define file paths relative to the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')

def read_json_data():
    """Reads and parses product data from a JSON file."""
    if not os.path.exists(JSON_FILE):
        return None
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return None

def read_csv_data():
    """Reads and parses product data from a CSV file."""
    if not os.path.exists(CSV_FILE):
        return None
    data = []
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert 'id' and 'price' to appropriate types
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    # Skip invalid rows or log error
                    continue
                data.append(row)
        return data
    except IOError:
        return None

@app.route('/products')
def products():
    """
    Handles the /products route, reading data based on 'source' query parameter
    and filtering by 'id'.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    # 1. Handle Invalid Source
    if source not in ['json', 'csv']:
        # Pass an error message directly to the template
        return render_template('product_display.html', error="Wrong source", products=[])

    # 2. Read Data
    if source == 'json':
        all_products = read_json_data()
    elif source == 'csv':
        all_products = read_csv_data()
    
    if all_products is None:
        # Handle case where file is missing or corrupted
        return render_template('product_display.html', error=f"Could not load data from {source} file.", products=[])

    # 3. Filter Data by ID
    display_products = []
    
    if product_id_str:
        # If an id is provided, attempt to filter
        try:
            product_id = int(product_id_str)
            
            # Find the specific product
            filtered_product = next((p for p in all_products if p.get('id') == product_id), None)
            
            if filtered_product:
                # If found, wrap it in a list for display
                display_products = [filtered_product]
            else:
                # Handle Product Not Found
                return render_template('product_display.html', error="Product not found", products=[])
                
        except ValueError:
            # Handle invalid non-integer id
            return render_template('product_display.html', error="Invalid product ID format.", products=[])
    else:
        # If no id is provided, display all products
        display_products = all_products

    # 4. Render Template
    return render_template('product_display.html', products=display_products, error=None)

# --- Routes from previous tasks (optional, but good for completeness) ---
@app.route('/')
def home():
    return "Welcome to the SSR File Viewer!"

if __name__ == '__main__':
    # Ensure data files are created for testing purposes
    # Create required data files
    products_data_json = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
        {"id": 3, "name": "T-Shirt", "category": "Apparel", "price": 25.00}
    ]
    
    products_data_csv = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
        {"id": 3, "name": "T-Shirt", "category": "Apparel", "price": 25.00}
    ]

    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(products_data_json, f, indent=4)
        
        with open(CSV_FILE, 'w', newline='') as f:
            fieldnames = ['id', 'name', 'category', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products_data_csv)
    except IOError as e:
        print(f"Could not create data files: {e}")
        
    app.run(debug=True, port=5000)
