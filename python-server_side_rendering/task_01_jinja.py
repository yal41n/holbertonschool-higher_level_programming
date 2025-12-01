from flask import Flask, render_template

# Create a Basic Flask Application
app = Flask(__name__)

# --- Routes ---

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

if __name__ == '__main__':
    # Run the Flask development server on port 5000 with debug mode
    app.run(debug=True, port=5000)
