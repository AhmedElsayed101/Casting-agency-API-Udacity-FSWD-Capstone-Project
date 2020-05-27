from flask import (render_template,
                   jsonify,
                   redirect, abort,
                   request
                   )
from app import app
from database.models import *
from .auth import requires_auth



@app.route('/api')
@requires_auth('')
def api():
    return jsonify({
        'message': 'Hello, Capstone!'
    })


@app.route('/login')
def login():
    url = "https://ayat101.auth0.com/authorize?audience=coffee&response_type=token&client_id=72qvFBzX50vyoVDJqc3wQoBsPjpCMBZY&redirect_uri=https://127.0.0.1:8100/tabs/user-page"
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
def get_all_actors():

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
def create_new_actor():

    data = request.get_json()
    try:
        actor_name = data['name']
        actor_age = data['age']
        actor_gender = data['gender']
    except:
        abort(401)

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
def get_actor(actor_id):

    current_actor = Actor.query.get(actor_id)
    if current_actor is None:
        abort(404)
    current_actor_formatted = current_actor.format()
    return jsonify({
        "actor": current_actor_formatted
    })


@app.route('/api/actors/<int:actor_id>', methods=['DELETE'])
def delete_new_actor(actor_id):

    current_actor = Actor.query.get(actor_id)
    if current_actor is None:
        abort(404)

    current_actor.delete()
    return jsonify({
        "success": True,
        "deleted": actor_id
    })


@app.route('/api/actors/<int:actor_id>', methods=['PATCH'])
def edit_new_actor(actor_id):

    data = request.get_json()

    current_actor = Actor.query.get(actor_id)

    try:
        actor_name = data['name']
        actor_age = data['age']
        actor_gender = data['gender']

    except:
        abort(401)

    current_actor.name = actor_name,
    current_actor.age = actor_age,
    current_actor.gender = actor_gender

    current_actor.update()

    return jsonify({
        "success": True,
        "updated": current_actor.id
    })


@app.route('/api/movies')
def get_all_movies():

    movies = Movie.query.order_by(Movie.id).all()

    if len(movies) == 0:
        abort(404)

    movies_formatted = [movie.format() for movie in movies]

    return jsonify({

        "success": True,
        "movies": movies_formatted,
        "movies_number": len(movies_formatted)
    })
    return jsonify({
        "actors": "all movies"
    })


@app.route('/api/movies', methods=['POST'])
def create_new_movie():

    data = request.get_json()
    try:
        movie_title = data['title']
        movie_start_time = data['start_time']
    except:
        abort(401)

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
def get_movie(movie_id):

    current_movie = Movie.query.get(movie_id)
    if current_movie is None:
        abort(404)
    current_movie_formatted = current_movie.format()
    return jsonify({
        "movie": current_movie_formatted
    })


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_new_movie(movie_id):

    current_movie = Movie.query.get(movie_id)
    if current_movie is None:
        abort(404)

    current_movie.delete()
    return jsonify({
        "success": True,
        "deleted": movie_id
    })


@app.route('/api/movies/<int:movie_id>', methods=['PATCH'])
def edit_new_movie(movie_id):

    data = request.get_json()

    current_movie = Movie.query.get(movie_id)

    try:
        movie_title = data['title']
        movie_start_time = data['start_time']
    except:
        abort(401)

    current_movie.title = movie_title
    current_movie.start_time = movie_start_time

    current_movie.update()

    return jsonify({
        "success": True,
        "updated": current_movie.id
    })
