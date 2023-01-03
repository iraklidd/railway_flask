from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
load_dotenv()
import os


# chemi klasebi
import webscrap




PWD = os.getenv("parolie")
# PWD = "comiti2"

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():

	contentdata = {
	 'content': 'index',
	 'subcontent': '',
	 'title': 'DS',
	}

	return render_template('index.html', **contentdata)


@app.route('/scrap', methods=["post", "get"])
def getscraping():

	contentdata = {
	 'content': 'scrap',
	 'subcontent': 'fnum',
	 'title': 'Web Scraping',
    }

	return render_template('index.html', **contentdata)








if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
