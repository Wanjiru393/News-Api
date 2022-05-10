from flask import render_template,url_for
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    news=get_news()

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html',articles=news) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404


@app.route('/sources')
def sources_page():

    sources = get_sources()

    return render_template('sources.html', sources=sources)


@app.route('/everything')
def everything():

    return render_template('everything.html')


@app.route('/business')
def business():

    Business = get_everything('business')
    return render_template('business.html', Business=Business)


@app.route('/technology')
def technology():

    technologies = get_everything('technology')
    return render_template('technology.html', technologies=technologies)


@app.route('/entertainment')
def entertainment():

    entertainments = get_everything('entertainment')
    return render_template('entertainment.html', entertainments=entertainments)


@app.route('/sports')
def sports():

    sports = get_everything('sports')
    return render_template('sports.html', sports=sports)


