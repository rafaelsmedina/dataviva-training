from app import app
from flask import render_template, request
from app.modules.models import User
from flask import render_template
from app.forms import LoginForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for
from app import db
from app.forms import RegistrationForm

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('base/base.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile/profile.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register/register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')

        return redirect(next_page)
        # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # return redirect(url_for('home'))
        
    return render_template('login/login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))