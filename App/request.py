from app import app
import urllib.request,json
from .models import news

News = news.News
Everything=news.Everything

# Getting api key
api_key = '3ca69fda5fa74125b35d01d178d09d42'

# Getting the movie base url
base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

#evrything on news API
all_url = 'https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey={}'

