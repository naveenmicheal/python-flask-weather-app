import requests
import json
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

api_url = 'http://api.openweathermap.org/data/2.5/weather'
apiid = 'xxxxxxxxxxxxxxxxxx'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
	location = request.form.get('location')
	responce = requests.get(url = api_url, params= dict(q= location, APPID = apiid))
	if responce.status_code !=200:
		print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' 
		return render_template('result.html', msg = 'Wrong Name', wloc = 'None', wtemp = 'None',wdis='None', prs='None' ,wspeed = 'None')
	data = responce.json()
	wloc = data['name']	
	wtemp = data['main']['temp']
	wdis =  data['weather'][0]['description']
	prs = data['main']['pressure']
	wspeed = data['wind']['speed']
	# print (wloc)
	# print (wtemp)
	# print (wdis)
	# print (prs)
	# print (wspeed)		
	return render_template('result.html',wloc = wloc, wtemp = wtemp,wdis=wdis, prs=prs ,wspeed = wspeed)

if __name__ == '__main__':
	app.run(debug = True)	
