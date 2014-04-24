from flask import Flask
import urllib2
from BeautifulSoup import BeautifulSoup
import json
import string

app = Flask(__name__)

@app.route('/games',methods=['GET'])
def index():
	return json_tag()
#return "Hello, World!"

@app.route('/games/<game_title>',methods=['GET'])
def get_score(game_title):
	raw_list = json.loads(json_tag())
	for i in raw_list:
		if game_title in i:
			return json.dumps(i)
		#if i[game_title].has_key:
			#return json.dumps(i)

def json_tag():
        html_page = urllib2.urlopen("http://www.metacritic.com/game/playstation-3").read()
	op_list = []
        for element in BeautifulSoup(html_page).findAll('tr'):
                if element.find('span', {'class' : 'metascore_w small game positive'}):
                        score = element.find('span', {'class' : 'metascore_w small game positive'}).contents[0]
                        #have to write logic for try and expect for contents will be Null
                        if element.find('a', {'class' : 'product_title'}):
                                title =  element.find('a', {'class' : 'product_title'}).contents[0].rstrip().lstrip()
				op_list.append({title:score})
        return json.dumps(op_list)
print json_tag()
if __name__ == '__main__':
    app.run(debug = True)
