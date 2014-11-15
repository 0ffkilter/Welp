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

def reducer(eateries): #list of dictionaries, cuts it down to the most mediocre three restaurants for that category
	p = len(eateries)

	eateries.sort(key=operator.itemgetter('rating'))
	x = p
	while x > 3:
		eateries = eateries[:-1]
		x = len(eateries)
	else:
		return eateries


def get_search_parameters(lat, long, foods):
	params = {}
	params["term"] = "restaurants"
	params["ll"] = "{},{}".format(str(lat), str(long))
	params["radius_filter"] = "40000"
	params["limit"] = "20"
	params["offset"] = "30"
	params["sort"] = 2
	params["category_filter"] = foods

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

	return data


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
		locations = [(34.1100,-117.7197)] 
		mehfoods = ['tradamerican', 'italian', 'chinese']
		if len(mehfoods) = 0:
			 mehfoods = ['tradamerican', 'italian', 'indpak', 'norwegian', 'greek','thai', 'mexican', 'chinese', 'japanese', 'pizza', 'diners']
		api_calls = []
		bizlist = []
		nbizlist = []
		n = len(mehfoods)
		for x in range (0,n):
			cat = mehfoods[x]
			for lat, long in locations:
					params = get_search_parameters(lat, long, cat)
					api_calls.append(get_results(params))
					eateries = api_calls[x][u'businesses']#.sort(key=operator.itemgetter('rating'))
					api_calls[x][u'businesses'] = reducer(eateries)
					time.sleep(1.0)
			
			l = len(api_calls[x][u'businesses'])
			bizlist.append(api_calls[x][u'businesses'])
		h = len(bizlist)
		for z in range (0, h):
			nbizlist += bizlist[z]

		nbizlist.sort(key=operator.itemgetter('distance'))

	return render_template('index.html', food_form = foodForm)

@welp.route('/results', methods=['GET', 'POST'])
def results():
	return render_template('results.html')
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




