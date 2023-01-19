from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/profile')
def teste():
    return render_template('profile/profile.html')

app.run(debug=True)