from flask import render_template
from flask import jsonify

<<<<<<< HEAD:app/views.py
from app import app
import rauth
import time

=======
from welp import welp
>>>>>>> 581aa39b07497f71b08b4e0d1892ee36fb512af1:welp/views.py

@welp.route('/')
def index():
    return render_template('index.html')



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
	params["term"] = "restaurants"
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

	return data

# if __name__=="__main__":
# 	main()
