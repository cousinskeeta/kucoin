"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import date
import pandas as pd
from coinscraper import coinscrapper

app = Flask(__name__, static_folder='data')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 
'password')
app.config['DATA'] = 'data/images'
global now 
now = date.today()

global summary
summary = pd.read_csv('data/summary.csv')
summary.drop(['Unnamed: 0'], inplace=True, axis=1)
print(summary.head())

global client
client = coinscrapper(now.strftime("%Y%m%d"))
print(type(client))


###
# Routing for your application.
###

@app.route('/')
@app.route('/home')
def home():
    """Render website's home page."""
    return render_template('home.html', date="", top10="",table="", 
    assets="",tables="", preds="", tables_="")

@app.route('/scrape_coins', methods=['GET','POST'])
def scrape_coins():
	date = now
	table = [summary.head(10).to_html(classes='saved', header="true")]
	tables = [summary.to_html(classes='saved', header="true")]

	return render_template('home.html', date="2020-08-20", 
    top10="Here are our top 10 picks from:\n",table=table, 
    assets="Here all the assets we assessed:\n",tables=tables )

@app.route('/update', methods=['GET','POST'])
def update():
    updated = client.summary()
    date = now
    updated.sort_values('RSI').to_csv('summary-{}.csv'.format(now))
    table = [updated.head().to_html(classes='data', header="true")]
    tables = [updated.to_html(classes='data', header="true")]
    return render_template('home.html', date=date, 
    top10="Here are our top 10 picks for:\n",table=table, 
    assets="Here all the assets we assessed:\n",tables=tables )


@app.route('/preds',methods=['GET','POST'])
def preds():
    print('RES-1')
    date = now
    print(date)
    name = str(request.form['url'])
    print(name)
    res = client.prediction(name)
    print(res)
    preds = res[2]
    print("Predictions: ",preds)
    tables_ = [res[0].tail(7).to_html(classes='preds', header="true")]
    print("Table: ", tables_)
    return render_template('home.html', date=date, top10="Here is our prediction:",preds=preds, assets="Here a table:\n",tables=tables_ )


###
# The functions below should be applicable to all Flask apps.
###

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
