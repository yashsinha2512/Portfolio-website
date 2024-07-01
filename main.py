from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/passreset')  # Define the passreset route
def passreset():
    return render_template('passreset.html')

@app.route('/home')  # Define the home page after login
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
