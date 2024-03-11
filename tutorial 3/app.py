# Importing flask from Flask module
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        username_input = request.form['username']
        print(username_input)
        return redirect(url_for('home'))
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)