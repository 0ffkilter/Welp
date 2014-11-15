from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField, RadioField
from wtforms.validators import Required, Email, EqualTo

class PreferencesForm(Form):
	food0 = RadioField('Food0', choices=[('love',''),('meh',''),('hate','')])

# class RegisterForm(Form):
# 	teamname = TextField('Team Name', validators=[Required()])
# 	names = TextField('Names', validators=[Required()])
# 	languages = SelectMultipleField('Languages', validators=[], choices=[
# 			('python', 'Python'),
# 			('java', 'Java'),
# 			('javascript', 'JavaScript')
# 		])
# 	email = TextField('Email', validators=[Required(), Email()])
# 	password = PasswordField('Password', validators=[Required()])
# 	confirm = PasswordField('Confirm', validators=[
# 		Required(), EqualTo('password', message='Passwords do not match.')])
# 	test = RadioField('Label', choices=[('value','description'),('value_two','whatever')])

# class LoginForm(Form):
# 	teamname = TextField('Team Name', validators=[Required()])
# 	password = PasswordField('Password', validators=[Required()])