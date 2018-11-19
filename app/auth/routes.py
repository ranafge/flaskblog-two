from flask import render_template, flash, redirect, url_for
from app import  db
from flask_login import (current_user, login_user, logout_user, login_required)
from app.models import User
from app.auth.forms import (RegistrationForm, LoginForm,
                            ResetPasswordRequestForm)
from app.email import send_password_reset_email
from flask_babel import _
from app.auth import bp



@bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        flash(_('You have successfully logged in.'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.usersprofile'))

    return render_template('auth/login.html', title= _('Sign In'), form=form)


@login_required
@bp.route('/logout')
def logout():
    logout_user()
    flash(_('You have successfully logout.'))
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, You may now a registered user!'))
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title= _('Register'), form=form)



@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_('Check your email for the instructions to reset your password.'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title=_('Reset password'), form=form)



@bp.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)
















