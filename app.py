from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')  # Show form on GET request

if __name__ == "__main__":
    app.run()
