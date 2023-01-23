from app import app
from flask import render_template, request
from app.modules.models import User
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    user = User.query.filter_by(username="john").first()
    return render_template('base/base.html')

@app.route('/profile')
def profile():
    return render_template('profile/profile.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login/login.html', title='Sign In', form=form)


