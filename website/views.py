from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for, session
from .db_connection import connect
import json
import pandas as pd
import numpy as np

views = Blueprint('views', __name__)
connect, cursor = connect()


@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template("landing.html")

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("homepage.html")

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        genre = request.form.get('genres')
        release_date = request.form.get('release_date')
        avg_vote = request.form.get('avg_vote')
    return render_template("search.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method =='GET':
        cursor.execute(
            "SELECT title, movie_id, tmdb_id FROM moviegenie.movies JOIN moviegenie.links WHERE moviegenie.title = %s "
            )
        results = cursor.fetchmany(10)
        ld = [dict(zip(('title','movie_id','tmdb_id'), values)) for values in results]
        print(ld)
        return render_template('movie_results.html',movie_info= ld)