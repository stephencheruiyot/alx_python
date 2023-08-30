"""Flask Web Application
This is a simple Flask web application that
displays "Hello HBNB!" when you access the root URL.
"""
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Route definition for the root URL ("/") with strict_slashes set to False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Main entry point of the script
if __name__ == '__main__':
    # Start the Flask web application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
