from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you can handle the form data submission if necessary
        # For example: send an email or save the data to a database
        print("Form submitted!")
    return render_template('contact.html')  # Show form on GET request

@app.route('/test')
def test_template():
    return render_template('home.html')


if __name__ == "__main__":
    # Use host='0.0.0.0' for deployment on cloud platforms like Render
    app.run(host='0.0.0.0', debug=True)
