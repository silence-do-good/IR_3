import urllib2
import tokenizer
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('search.html')

@app.route('/search', methods = ['POST'])
def search():
    query = request.form['query']
    url_list = tokenizer.getqueryResult(query)
    url_list = ["https://" + s for s in url_list]
    return render_template('results.html',url_list = url_list)

if __name__ == "__main__":
    app.run()
