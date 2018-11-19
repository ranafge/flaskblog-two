from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_babel import _, gettext as _l
from app.models import User
from flask import request



class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[DataRequired(), Length(min=0, max=250)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self,username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.original_username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    post = TextAreaField(_l('Say something'), validators=[DataRequired(), Length(min=1, max=1500)])
    submit = SubmitField(_l('Submit'))



class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)






























