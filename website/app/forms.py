from flask.ext.wtf import Form, RecaptchaField
from wtforms import BooleanField, StringField, TextField, PasswordField, validators
from wtforms.validators import DataRequired,InputRequired, Email, URL
from wtforms.fields.html5 import EmailField, URLField
from wtforms.fields import SelectField, StringField
from wtforms.widgets import TextArea 
from flask.ext.login import current_user
from models import app_users
from server import db
from app import bcrypt


class LoginForm(Form):
    email = EmailField('Email Address', [validators.Required(), validators.Email(), validators.Length(min=1, max=35)])
    password = PasswordField('Password', [validators.Required()])
    
    def validate(self):
    	if not Form.validate(self):
      		return False

		
    	user = app_users.query.filter_by(email = self.email.data).first()
    	
    	
    	if user and bcrypt.check_password_hash(user.pw, self.password.data):
    		return True
    	else:
			self.email.errors.append("Invalid e-mail or password")
			return False



class RegistrationForm(Form):
	email = EmailField('Email Address', [validators.Required(), validators.Email(), validators.Length(min=1, max=35)])
	password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password', [validators.Required(), validators.EqualTo('password', message='Passwords must match')])
	def validate(self):
		if not Form.validate(self):
			return False
      		
		#check if username/email is taken or not
		if app_users.query.filter_by(email = self.email.data).first() is not None:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True


class SearchForm(Form):
	search = StringField('search', validators=[DataRequired()])

class ResetPasswordForm(Form):
	
	old_password = PasswordField('Old Password', [validators.Required()])
	new_password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password', [validators.Required(), validators.EqualTo('new_password', message='Passwords must match')])
	def validate(self):
		if not Form.validate(self):
			return False
		user = app_users.query.filter_by(email = current_user.email).first()
		if user and bcrypt.check_password_hash(user.pw, self.old_password.data):
			return True
		else:
			self.old_password.errors.append("Invalid password")
		return False

class ResetEmailForm(Form):
	
	
	password = PasswordField('Password', [validators.Required()])
	new_email = EmailField('New Email Address', [validators.Required(), validators.Email()])
	
	def validate(self):
		if not Form.validate(self):
			return False
		user = app_users.query.filter_by(email = current_user.email).first()
		if user and bcrypt.check_password_hash(user.pw, self.password.data):
			return True
		else:
			self.password.errors.append("Invalid password")
		return False


class CreateCourseForm(Form):
	name = StringField('Name', [validators.Required(),validators.Length(min=1, max=35)])
	description = StringField('Description', [validators.Required()], widget=TextArea())
	category_id = SelectField('CategoryId', coerce=int, choices=[(1, 'Design'),(2, 'Web'),(3, 'Business'), (4, '3D+Animation'), (5,'Music')])

	def validate(self):
		if not Form.validate(self):
			return False
		return True
