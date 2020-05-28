from flask import (render_template,
                   jsonify,
                   redirect, abort,
                   request
                   )
from app import app
from database.models import *
from .auth import requires_auth, token_required
import os


@app.route('/api')
@token_required
def api(payload):
    return jsonify({
        'message': 'Hello, Capstone!'
    })


@app.route('/login')
def login():
    audience = os.environ.get('API_AUDIENCE')
    domain = os.environ.get('AUTH0_DOMAIN')
    client_id = os.environ.get('CLIENT_ID')
    redirect_url = os.environ.get('REDIRECT_URL')
    
    part1 = f"https://{domain}/authorize?audience={audience}"
    part2 = f"&response_type=token&client_id={client_id}"
    part3 = f"&redirect_uri={redirect_url}"
    url = part1+part2+part3

    return redirect(url)

# @app.route('/api/actors/new')
# def add_actor_info():
#     # get users info from auth0 to store in database
#     return jsonify({
#         "actors":"all actors"
#     })


@app.route('/logout')
def logout():
    return jsonify({
        'message': 'You are logged out'
    })


@app.route('/api/actors')
@requires_auth('view:actor')
def get_all_actors(payload):

    actros = Actor.query.order_by(Actor.id).all()

    if len(actros) == 0:
        abort(404)

    actors_formatted = [actor.format() for actor in actros]

    return jsonify({

        "success": True,
        "actors": actors_formatted,
        "actors_number": len(actors_formatted)
    })


@app.route('/api/actors', methods=['POST'])
@requires_auth('add:actor')
def create_new_actor(payload):

    data = request.get_json()
    try:
        actor_name = data['name']
        actor_age = data['age']
        actor_gender = data['gender']
    except:
        abort(400)

    new_actor = Actor(
        name=actor_name,
        age=actor_age,
        gender=actor_gender
    )

    new_actor.insert()

    return jsonify({
        "success": True,
        "created": new_actor.id
    })


@app.route('/api/actors/<int:actor_id>', methods=['GET'])
@requires_auth('view:actor')
def get_actor(payload, actor_id):

    current_actor = Actor.query.get(actor_id)
    if current_actor is None:
        abort(404)
    current_actor_formatted = current_actor.format()
    return jsonify({
        "success": True,
        "actor": current_actor_formatted
    })


@app.route('/api/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_new_actor(payload, actor_id):

    current_actor = Actor.query.get(actor_id)
    if current_actor is None:
        abort(404)

    current_actor.delete()
    return jsonify({
        "success": True,
        "deleted": actor_id
    })


@app.route('/api/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('edit:actor')
def edit_new_actor(payload, actor_id):

    data = request.get_json()

    current_actor = Actor.query.get(actor_id)
    if current_actor is None:
        abort(404)

    try:
        actor_name = data['name']
        actor_age = data['age']
        actor_gender = data['gender']

    except:
        abort(400)

    current_actor.name = actor_name,
    current_actor.age = actor_age,
    current_actor.gender = actor_gender

    current_actor.update()

    return jsonify({
        "success": True,
        "updated": current_actor.id
    })


@app.route('/api/movies')
@requires_auth('view:movie')
def get_all_movies(payload):

    movies = Movie.query.order_by(Movie.id).all()

    if len(movies) == 0:
        abort(404)

    movies_formatted = [movie.format() for movie in movies]

    return jsonify({

        "success": True,
        "movies": movies_formatted,
        "movies_number": len(movies_formatted)
    })


@app.route('/api/movies', methods=['POST'])
@requires_auth('add:movie')
def create_new_movie(payload):

    data = request.get_json()
    try:
        movie_title = data['title']
        movie_start_time = data['start_time']
    except:
        abort(400)

    new_movie = Movie(

        title=movie_title,
        start_time=movie_start_time
    )

    new_movie.insert()

    return jsonify({
        "success": True,
        "created": new_movie.id
    })


@app.route('/api/movies/<int:movie_id>', methods=['GET'])
@requires_auth('view:movie')
def get_movie(payload, movie_id):

    current_movie = Movie.query.get(movie_id)
    if current_movie is None:
        abort(404)
    current_movie_formatted = current_movie.format()

    return jsonify({
        "success": True,
        "movie": current_movie_formatted
    })


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_new_movie(payload, movie_id):

    current_movie = Movie.query.get(movie_id)
    if current_movie is None:
        abort(404)

    current_movie.delete()
    return jsonify({
        "success": True,
        "deleted": movie_id
    })


@app.route('/api/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('edit:movie')
def edit_new_movie(payload, movie_id):

    data = request.get_json()

    current_movie = Movie.query.get(movie_id)

    if current_movie is None:
        abort(404)

    try:
        movie_title = data['title']
        movie_start_time = data['start_time']
    except:
        abort(404)

    current_movie.title = movie_title
    current_movie.start_time = movie_start_time

    current_movie.update()

    return jsonify({
        "success": True,
        "updated": current_movie.id
    })
