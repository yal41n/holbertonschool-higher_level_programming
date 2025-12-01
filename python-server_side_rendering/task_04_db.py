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

# --- Database Setup Utility ---

def create_database():
    """Creates the SQLite database and populates the Products table."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # 1. Create Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # 2. Insert Data (Delete existing data first to prevent duplicate primary keys)
        cursor.execute('DELETE FROM Products')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Wireless Mouse', 'Electronics', 25.50)
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during creation/population: {e}")
    finally:
        if conn:
            conn.close()

# --- File Reading Functions (Reused from Task 3) ---

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

# --- New: SQLite Reading Function ---

def read_sql_data(product_id=None):
    """Reads product data from the SQLite database."""
    products = []
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        # Use sqlite3.Row to allow accessing columns by name
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = 'SELECT id, name, category, price FROM Products'
        params = []
        
        if product_id is not None:
            query += ' WHERE id = ?'
            params.append(product_id)
            
        cursor.execute(query, params)
        
        # Convert sqlite3.Row objects to dictionaries
        for row in cursor.fetchall():
            products.append(dict(row))
        
        return products
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# --- Products Route (Updated) ---

@app.route('/products')
def products():
    """
    Handles the /products route, reading data based on 'source' 
    query parameter and filtering by 'id'. Now supports 'json', 'csv', and 'sql'.
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
        # Fetch from SQL (filter logic applied later if ID is passed)
        all_products = read_sql_data()
        
    if all_products is None:
        # Handle case where file/DB is missing or corrupted
        return render_template('product_display.html', error=f"Could not load data from {source}.", products=[])

    # 3. Filter Data by ID (applies to JSON and CSV)
    display_products = []
    
    if product_id_str:
        # If an id is provided, attempt to filter
        try:
            product_id = int(product_id_str)
            
            # Use filter comprehension for JSON/CSV data (SQL data is filtered by the query)
            filtered_product = next((p for p in all_products if p.get('id') == product_id), None)
            
            if filtered_product:
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

# --- Home Route ---
@app.route('/')
def home():
    return "Welcome to the SSR Data Viewer! Use /products?source=[json|csv|sql]"

if __name__ == '__main__':
    # 1. Ensure DB file exists and is populated
    create_database()
    
    # 2. Create sample JSON/CSV files if needed for testing (Optional, but useful)
    try:
        products_data_json = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Wireless Mouse", "category": "Electronics", "price": 25.50}
        ]
        
        with open(JSON_FILE, 'w') as f:
            json.dump(products_data_json, f, indent=4)
        
        with open(CSV_FILE, 'w', newline='') as f:
            fieldnames = ['id', 'name', 'category', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products_data_json)
    except IOError as e:
        print(f"Could not create data files: {e}")
        
    # 3. Run the Flask application
    app.run(debug=True, port=5000)
