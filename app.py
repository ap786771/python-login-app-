from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    user = request.form['username']
    pwd = request.form['password']
    if user == 'admin' and pwd == 'admin123':
        return render_template('success.html', user=user)
    return "Login Failed", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
