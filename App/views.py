from flask import render_template,url_for
from app import app
from .request import get_News

# Views
@app.route('/')
def index():

    news=get_News()

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html',articles=news) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404