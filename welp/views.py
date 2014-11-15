from flask import render_template
from flask import jsonify
from flask import request

import rauth
import time

from welp import welp
from forms import PreferencesForm

foodPrefs = {'American':'meh', 'Chinese':'meh', 'Diner':'meh', 'Greek':'meh', 'Italian':'meh', 'Japanese':'meh', 'Traditional Norwegian':'meh', 'Mexican':'meh', 'Pizza':'meh', 'Thai':'meh', 'Indian':'meh'}
terms = {'American':'tradamerican', 'Chinese':'chinese', 'Diner':'diners', 'Greek':'greek', 'Italian':'italian', 'Japanese':'japanese', 'Traditional Norwegian':'norwegian', 'Mexican':'mexican', 'Pizza':'pizza', 'Thai':'thai', 'Indian':'indpak'}
mehFoods = ""
location = []

@welp.route('/')
def index():
	location = request.args.get('location')
	print location
	return render_template('index.html', foodPrefs=foodPrefs, location=location)

@welp.route('/', methods=['POST'])
def food_prefs():
	mehFoods = ""

	for food, pref in foodPrefs.iteritems():
		newPref = request.form[food]
		foodPrefs[food] = newPref
		if newPref == 'meh':
			mehFoods += food
			mehFoods += ' '

	print mehFoods
	# location = request.args.get('location')
	return render_template('index.html', foodPrefs=foodPrefs, location=location)


def main(): 
		locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
		api_calls = []
		for lat, long in locations:
				params = get_search_parameters(lat, long)
				api_calls.append(get_results(params))
				time.sleep(1.0)
		print api_calls[0][u'region'][u'span'][u'latitude_delta']


def get_search_parameters(lat, long):
	params = {}
	params["term"] = "restaurants " + mehFoods
	params["ll"] = "{},{}".format(str(lat), str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "10"

	return params

def get_results(params):
	consumer_key = "TwiZjmvAvrct4Xu6OxN49w" 
	consumer_secret = "Ul7lj0H4wBdvPdY8Ci9eZkdI4tE"
	token = "B93gZUtPLgD5KRc-IwBicN3qt30xUt2B"
	token_secret = "p_gv7ofsb_LAfl-_u8hL30ezLrY"

	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)

	request = session.get("http://api.yelp.com/v2/search", params = params)

	data = request.json()
	session.close()

	print data

	return data

# if __name__=="__main__":
# 	main()
