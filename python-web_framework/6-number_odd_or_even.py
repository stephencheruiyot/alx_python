"""Flask Web Application"""
from flask import Flask, render_template
app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route to display "C <text>"
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

# Route to display "Python <text>"
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

# Route to display "<n> is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

# Route to display an HTML page with "<n> is even|odd" inside an H1 tag
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even='odd')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
