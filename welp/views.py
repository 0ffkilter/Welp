from flask import render_template
from flask import jsonify
from flask import request

import rauth
import time

from welp import welp
from forms import PreferencesForm

from werkzeug.contrib.cache import SimpleCache

CACHE_TIMEOUT = 300

cache = SimpleCache()

class cached(object):

    def __init__(self, timeout=None):
        self.timeout = timeout or CACHE_TIMEOUT

    def __call__(self, f):
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator

@welp.route('/', methods=['GET', 'POST'])
def index():
	foodForm = PreferencesForm(csrf_enabled=False)
	location = request.args.get('location')
	cache.set('location', location, timeout = 10 * 60)
	if (request.method == "POST"):
		lst = []
		if (foodForm.indpak.data == "meh"):
			lst += ["indpak"]
		if (foodForm.greek.data == "meh"):
			lst += ["greek"]
		if (foodForm.thai.data == "meh"):
			lst += ["thai"]
		if (foodForm.tradamerican.data == "meh"):
			lst += ["tradamerican"]
		if (foodForm.italian.data == "meh"):
			lst += ["italian"]
		if (foodForm.norwegian.data == "meh"):
			lst += ["norwegian"]
		if (foodForm.mexican.data == "meh"):
			lst += ["mexican"]
		if (foodForm.chinese.data == "meh"):
			lst += ["chinese"]
		if (foodForm.japanese.data == "meh"):
			lst += ["japanese"]
		if (foodForm.pizza.data == "meh"):
			lst += ["pizza"]
		if (foodForm.diners.data == "meh"):
			lst += ["diners"]
		cache.set('foodChoices', lst, timeout = 10 * 60)

	return render_template('index.html', food_form = foodForm)


# @welp.route('/', methods=['GET'])
# def food_prefs():
# 	mehFoods = ""
# 	for food, pref in foodPrefs.iteritems():
# 		newPref = request.form[food]
# 		foodPrefs[food] = newPref
# 		if newPref == 'meh':
# 			mehFoods += food
# 			mehFoods += ' '

# 	print mehFoods
	# location = request.args.get('location')


@welp.route('/results', methods=['GET', 'POST'])
def results():
	pass



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
