from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            error_msg = 'Invalid username or password'
            return render_template('login.html', error_msg=error_msg)
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        errors = []
        if not isinstance(name, str) or len(name) < 5:
            errors.append('Name must be a string with at least 5 characters')
        if not email.endswith('@gmail.com'):
            errors.append('Email must end with @gmail.com')
        if not password:
            errors.append('Password is required')
        if password != confirm_password:
            errors.append('Passwords do not match')
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long')
        
        if errors:
            # Render the signup form with error messages
            return render_template('signup.html', errors=errors)
        else:
            return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)