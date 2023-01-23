from app import app
from flask import render_template, request
from app.modules.models import User


@app.route('/', methods=['GET'])
def home():
    user = User.query.filter_by(username="john").first()
    print(user)
    return render_template('home/home.html', username=user.username)


@app.route('/profile')
def profile():
    return render_template('profile/profile.html')


if __name__ == '__main__':
    app.run(debug=True)
