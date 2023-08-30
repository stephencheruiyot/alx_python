from flask import Flask

app = Flask(__name__)

# Define the route for the home page
@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
