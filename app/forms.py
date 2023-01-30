from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, Field
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, DataRequired, Length
from app.modules.models import User
from markupsafe import Markup, escape
from wtforms.widgets.core import html_params


class EmptyForm(FlaskForm):
    submit = SubmitField('Enviar')


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')


class EditProfileForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    about_me = TextAreaField('Sobre mim', validators=[Length(min=0, max=140)])
    submit = SubmitField('Salvar')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class InlineButtonWidget(object):
    def __init__(self, class_=None):
        self.class_ = class_

    def __call__(self, field, **kwargs):
        kwargs.setdefault('type', 'submit')
        kwargs["class"] = self.class_
        title = kwargs.pop('title', field.description or '')
        params = html_params(title=title, **kwargs)

        html = '<button %s>%s</button>'
        return Markup(html % (params, escape(field.label.text)))


class InlineButton(Field):
    widget = InlineButtonWidget()

    def __init__(self, label=None, validators=None, text='Save', **kwargs):
        super(InlineButton, self).__init__(label, validators, **kwargs)
        self.text = text

    def _value(self):
        if self.data:
            return u''.join(self.data)
        else:
            return u''

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Repetir senha', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                'Por favor use um nome de usuário diferente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'Por favor use um endereço de email diferente.')


class PostForm(FlaskForm):
    style = {'style': 'width:100%; padding: 8px; resize: none;'}
    post = TextAreaField(validators=[
        DataRequired(), Length(min=1, max=140)], render_kw=style, label="O que que pega?")
    text = Markup('<i class="fas fa-sign-in-alt"></i> Publicar')
    submit = SubmitField(
        text, widget=InlineButtonWidget(class_="btn btn-info"))
