from flask import Flask, render_template
import json
import os

# Create the Flask application
app = Flask(__name__)

# --- Reusing Routes from Task 01 (for completeness, assuming this is the final file) ---

@app.route('/')
def home():
    """Renders the home page (index.html)."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page (about.html)."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page (contact.html)."""
    return render_template('contact.html')

# --- New Route for Task 02 ---

@app.route('/items')
def items_list():
    """
    Reads item data from items.json and renders it using items.html.
    """
    data = {"items": []}  # Default empty list
    json_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
    
    # Check if the JSON file exists
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print("Error: Could not decode items.json. Using empty list.")
        except IOError:
            print("Error: Could not read items.json. Using empty list.")
    
    # Extract the list of items, defaulting to an empty list if the key is missing
    items = data.get("items", [])
    
    # Pass the items list to the template
    return render_template('items.html', items=items)

if __name__ == '__main__':
    # Run the Flask development server on port 5000 with debug mode
    # Ensure items.json exists in the same directory for this to run correctly
    app.run(debug=True, port=5000)
