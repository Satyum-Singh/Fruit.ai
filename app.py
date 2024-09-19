from flask import Flask, render_template, request, redirect, url_for, jsonify, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/signup', methods=['GET','POST'])
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

# In-memory FAQ storage (no database)
arr = [
    {'question': 'What is fruit.ai best for its services?', 'answer': 'becuase of proper and time to time customer support'},
    {'question': 'What is mango?', 'answer': 'Mango is yellow fibrous fruit and comes in diff shapes,sizes & types.'},
]

@app.route('/faqs', methods=['GET'])
def faqs():
    return render_template('faqs.html', questions=arr)

@app.route('/faqs', methods=['POST'])
def add_or_update_faq():
    data = request.form
    faq_id = data.get('id')
    
    if faq_id:
        faq_id = int(faq_id)
        arr[faq_id] = {'question': data['question'], 'answer': data['answer']}
    else:
        arr.append({'question': data['question'], 'answer': data['answer']})
    
    return redirect(url_for('faqs'))

@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global arr
    if 0 <= faq_id < len(arr):
        arr.pop(faq_id)
        return '', 204
    return '', 404

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

with open('fruit.json') as f:
    fruits = json.load(f)

@app.route('/get_fruit_info', methods=['GET'])
def get_fruit_info():
    fruit_name = request.args.get('fruit_name')
    fruit_info = get_fruit_info(fruit_name)
    if fruit_info:
        return jsonify(fruit_info)
    else:
        return jsonify({'error': 'Fruit not found'})

if __name__ == '__main__':
    app.run(debug=True)