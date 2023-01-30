from app import app, db
from flask import render_template, request, flash, redirect, url_for, g
from app.modules.models import User, Post
from app.forms import LoginForm, EditProfileForm, RegistrationForm, EmptyForm, PostForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Seu post foi publicado!')
        return redirect(url_for('home'))
    
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('home', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('home/home.html', title='Home', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    form = EmptyForm()
    return render_template('user/user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url, form=form)

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
        flash('Parabéns, você foi cadastrado com sucesso!')
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
            flash('Nome de usuário ou senha inválidos!')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')

        return redirect(next_page)
        
    return render_template('login/login.html', title='Entrar', form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Suas mudanças foram salvas.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile/edit_profile.html', title='Editar Perfil',
                           form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/follow/<username>', methods=['POST', 'GET'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('Usuário {} não foi encontrado.'.format(username))
            return redirect(url_for('home'))
        if user == current_user:
            flash('Você não pode parar de seguir você mesmo!')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('Você está seguindo {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('home'))

@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('Usuário {} não foi encontrado.'.format(username))
            return redirect(url_for('home'))
        if user == current_user:
            flash('Você não pode parar de seguir você mesmo!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('Você não está seguindo {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('home'))

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template("home/home.html", title='Explore', posts=posts.items,
                          next_url=next_url, prev_url=prev_url)

@app.route('/search')
@login_required
def search():
    # if not g.search_form.validate():
    #     return redirect(url_for('explore'))
    # page = request.args.get('page', 1, type=int)
    # posts, total = Post.search(g.search_form.q.data, page,
    #                            app.config['POSTS_PER_PAGE'])
    # next_url = url_for('search', q=g.search_form.q.data, page=page + 1) \
    #     if total > page * app.config['POSTS_PER_PAGE'] else None
    # prev_url = url_for('search', q=g.search_form.q.data, page=page - 1) \
    #     if page > 1 else None
    page = request.args.get('page', 1, type=int)
    users = User.query.filter(User.username.contains(g.search_form.q.data))
    posts = Post.query.filter(Post.body.contains(g.search_form.q.data)).order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template("home/home.html", title='Explore', posts=posts.items, next_url=next_url, prev_url=prev_url, search_users=users)