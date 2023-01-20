from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/profile')
def profile():
    return render_template('profile/profile.html')

if __name__ == '__main__':
    app.run(debug=True)