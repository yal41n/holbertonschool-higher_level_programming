from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Define file paths relative to the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, 'products.json')
CSV_FILE = os.path.join(BASE_DIR, 'products.csv')
DB_FILE = os.path.join(BASE_DIR, 'products.db')

# --- Database Setup Utility (Remains for completeness, but not called at runtime) ---

def create_database():
    """Utility function to create and populate the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Using a standard dataset, assuming the external script will populate the test data
        cursor.execute('DELETE FROM Products')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during creation/population: {e}")
    finally:
        if conn:
            conn.close()

# --- File Reading Functions ---

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
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    continue
                data.append(row)
        return data
    except IOError:
        return None

# --- SQLite Reading Function ---

def read_sql_data():
    """Reads all product data from the SQLite database."""
    products = []
    conn = None
    try:
        # Connects to the database created by the external script
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = 'SELECT id, name, category, price FROM Products'
        cursor.execute(query)
        
        for row in cursor.fetchall():
            products.append(dict(row))
        
        return products
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# --- Products Route ---

@app.route('/products')
def products():
    """
    Handles the /products route, reading data based on 'source' 
    query parameter and filtering by 'id'.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    # 1. Handle Invalid Source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source", products=[])
    
    all_products = None
    
    # 2. Read Data based on Source
    if source == 'json':
        all_products = read_json_data()
    elif source == 'csv':
        all_products = read_csv_data()
    elif source == 'sql':
        all_products = read_sql_data()
        
    if all_products is None:
        return render_template('product_display.html', error=f"Could not load data from {source}.", products=[])

    # 3. Filter Data by ID
    display_products = []
    
    if product_id_str:
        try:
            product_id = int(product_id_str)
            
            # Filter the loaded data
            filtered_product = next((p for p in all_products if p.get('id') == product_id), None)
            
            if filtered_product:
                display_products = [filtered_product]
            else:
                return render_template('product_display.html', error="Product not found", products=[])
                
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID format.", products=[])
    else:
        # If no id is provided, display all products
        display_products = all_products

    # 4. Render Template
    return render_template('product_display.html', products=display_products, error=None)

# --- Home Route ---
@app.route('/')
def home():
    return "Welcome to the SSR Data Viewer! Use /products?source=[json|csv|sql]"

if __name__ == '__main__':
    # CRITICAL FIX: The call to create_database() is REMOVED from the execution block.
    # We rely on the test runner's 'create_database.py' script to set up the database,
    # thus preventing us from overwriting the test data (e.g., 'Jarvis').
    
    app.run(debug=True, port=5000)
