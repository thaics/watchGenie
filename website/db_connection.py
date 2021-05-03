import pymysql
from pymysql import cursors
from pymysql.cursors import DictCursor
import json
import requests

API_KEY = '?api_key=1cf50e6248dc270629e802686245c2c8'
BASE_URL = 'https://api.themoviedb.org/3/movie/'
IMG_URL = 'https://image.tmdb.org/t/p/w500'

def connect():
    try:
        connect = pymysql.connect(
        user = 'root', password = 'tt156383', host = 'localhost', database = 'watchGenie',
        )
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        return connect, cursor
    except:
        print('Could not connect to database')
        return None

def get_movie_image(movie_id):
    searchURL = BASE_URL + str(movie_id) + API_KEY
    response = requests.get(searchURL)
    data = response.json()
    return IMG_URL + str(data['poster_path'])
