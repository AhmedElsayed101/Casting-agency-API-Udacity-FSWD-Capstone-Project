from flask import render_template,jsonify, redirect
from app import app
from database.models import *


@app.route('/api')
def api():
    return jsonify({
        'message':'Hello, Capstone!'
    })

@app.route('/login')
def login():
    url = "https://ayat101.auth0.com/authorize?audience=coffee&response_type=token&client_id=72qvFBzX50vyoVDJqc3wQoBsPjpCMBZY&redirect_uri=https://127.0.0.1:8100/tabs/user-page"
    return redirect(url)
    
@app.route('/logout')
def logout():
    return jsonify({
        'message': 'You are logged out'
    })


@app.route('/api/actors')
def get_all_actors():
    return jsonify({
        "actors":"all actors"
    })

@app.route('/api/actors', methods = ['POST'])
def create_new_actor():
    return jsonify({
        "actors":"all actors"
    })

@app.route('/api/actors/<int:actor_id>', methods = ['POST'])
def delete_new_actor(actor_id):
    return jsonify({
        "actors":"all actors"
    })

@app.route('/api/actors/<int:actor_id>', methods = ['PATCH'])
def edit_new_actor(actor_id):
    return jsonify({
        "actors":"all actors"
    })



@app.route('/api/movies')
def get_all_movies():
    return jsonify({
        "actors":"all movies"
    })

@app.route('/api/movies', methods = ['POST'])
def create_new_movie():
    return jsonify({
        "actors":"all movies"
    })

@app.route('/api/movies/<int:movie_id>', methods = ['POST'])
def delete_new_movie(movie_id):
    return jsonify({
        "actors":"all movies"
    })

@app.route('/api/movies/<int:movie_id>', methods = ['PATCH'])
def edit_new_movie(movie_id):
    return jsonify({
        "actors":"all movies"
    })

