# task_03_files.py

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Define file paths relative to the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')

# ... (read_json_data and read_csv_data functions remain the same) ...
def read_json_data():
    # ... (function body) ...
    if not os.path.exists(JSON_FILE):
        return None
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return None

def read_csv_data():
    # ... (function body) ...
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

# ... (products route remains the same) ...
@app.route('/products')
def products():
    # ... (function body) ...
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=[])
    
    # ... (rest of the products route logic) ...
    if source == 'json':
        all_products = read_json_data()
    elif source == 'csv':
        all_products = read_csv_data()
    
    if all_products is None:
        return render_template('product_display.html', error=f"Could not load data from {source} file.", products=[])

    display_products = []
    
    if product_id_str:
        try:
            product_id = int(product_id_str)
            filtered_product = next((p for p in all_products if p.get('id') == product_id), None)
            
            if filtered_product:
                display_products = [filtered_product]
            else:
                return render_template('product_display.html', error="Product not found", products=[])
                
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID format.", products=[])
    else:
        display_products = all_products

    return render_template('product_display.html', products=display_products, error=None)

@app.route('/')
def home():
    return "Welcome to the SSR File Viewer!"

if __name__ == '__main__':
    # REMOVE ALL CODE HERE THAT CREATES OR OVERWRITES products.json/products.csv
    # It will prevent the test runner's data from being used.
    app.run(debug=True, port=5000)
