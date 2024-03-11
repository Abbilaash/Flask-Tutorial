# Importing flask from Flask module
from flask import Flask, redirect, url_for

# create a flask app instance
# this app represents our web application
app = Flask(__name__)

# Now lets design the pages and routes
# first lets define the route for the home page
@app.route('/')
def home():
    return "<h1>Hello World!</h1>"

# grabbing value from url and passing it to the function
@app.route('/<name>')
def user(name):
    return f"<h1>Hello {name}!</h1>"

# redirecting to another page
@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__== '__main__':
    app.run(debug=True)