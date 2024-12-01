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
    if request.method == 'POST':
        print("Form submitted!")
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
