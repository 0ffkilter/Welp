from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField, RadioField


class PreferencesForm(Form):
	fchoices = [('love','love'),('meh','meh'),('hate','not feeling it')]
	indpak			= RadioField('Indian', choices=fchoices, default = "meh")
	greek 			= RadioField('Greek', choices=fchoices, default = "meh")
	thai			= RadioField('Thai', choices=fchoices, default = "meh")
	tradamerican	= RadioField('American', choices=fchoices, default = "meh")
	italian			= RadioField('Italian' , choices=fchoices, default = "meh")
	norwegian		= RadioField('Traditional Norwegian' , choices=fchoices, default = "meh")
	mexican			= RadioField('Cexican' , choices=fchoices, default = "meh")
	chinese			= RadioField('Chinese' , choices=fchoices, default = "meh")
	japanese		= RadioField('Japanese', choices=fchoices, default = "meh")
	pizza			= RadioField('Pizza', 	choices=fchoices, default = "meh")
	diners			= RadioField('Diners' ,	choices=fchoices, default = "meh")
