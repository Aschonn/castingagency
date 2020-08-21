import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import db_drop_and_create_all, setup_db, Actor, Movie, Performance
from config import pagination

ROWS_PER_PAGE = pagination['example']

def create_app(test_config=None):
  '''create and configure the app'''
  
  app = Flask(__name__)
  setup_db(app)


#----------- uncomment this if you want to start a new database on app refresh------------#


  db_drop_and_create_all() 



#--------- CORS (API configuration) -----------#


  CORS(app)
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response


#--------- Custom Functions -----------#



  def get_error_message(error, default_text):
    
    try:
        # Return message contained in error, if possible
        return error.description['message']
    except:
        # otherwise, return given default text
        return default_text

  def paginate_results(request, selection):

    # Get page from request. If not given, default to 1
    page = request.args.get('page', 1, type=int)
    
    # Calculate start and end slicing
    start =  (page - 1) * ROWS_PER_PAGE
    end = start + ROWS_PER_PAGE

    # Format selection into list of dicts and return sliced
    objects_formatted = [object_name.format() for object_name in selection]
    return objects_formatted[start:end]


#--------- Endpoints -----------#


  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):

    selection = Actor.query.all()
    actors_paginated = paginate_results(request, selection)

    if len(actors_paginated) == 0:
      abort(404, {'message': 'no actors found in database.'})

    return jsonify({
      'success': True,
      'actors': actors_paginated
    })

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def insert_actors(payload):

    body = request.get_json()

    if not body:
          abort(400, {'message': 'request does not contain a valid JSON body.'})

    # Extract name and age value from request body
    name = body.get('name', None)
    age = body.get('age', None)

    # Set gender to value or to 'Other' if not given
    gender = body.get('gender', 'Other')

    # abort if one of these are missing with appropiate error message
    if not name:
      abort(422, {'message': 'no name provided.'})

    if not age:
      abort(422, {'message': 'no age provided.'})

    # Create new instance of Actor & insert it.
    new_actor = (Actor(
          name = name, 
          age = age,
          gender = gender
          ))
    new_actor.insert()

    return jsonify({
      'success': True,
      'created': new_actor.id
    })

  @app.route('/actors/<actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actors(payload, actor_id):

    body = request.get_json()

    # Abort if no actor_id or body is not there
    if not actor_id:
      abort(400, {'message': 'please append an actor id to the request url.'})

    if not body:
      abort(400, {'message': 'request does not contain a valid JSON body.'})

    # Find actor which should be updated by id
    actor_to_update = Actor.query.filter(Actor.id == actor_id).one_or_none()

    # Abort 404 if actor id doesnt exists
    if not actor_to_update:
      abort(404, {'message': 'Actor with id {} not found in database.'.format(actor_id)})

    # Extract name and age value from request body
    name = body.get('name', actor_to_update.name)
    age = body.get('age', actor_to_update.age)
    gender = body.get('gender', actor_to_update.gender)

    # Set new field values
    actor_to_update.name = name
    actor_to_update.age = age
    actor_to_update.gender = gender

    # Delete actor with new values
    actor_to_update.update()

    # Return success, updated actor id and updated actor as formatted list
    return jsonify({
      'success': True,
      'updated': actor_to_update.id,
      'actor' : [actor_to_update.format()]
    })

  @app.route('/actors/<actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(payload, actor_id):

    # Abort if no actor_id has been provided
    if not actor_id:
      abort(400, {'message': 'please append an actor id to the request url.'})
  
    # Find actor which should be deleted by id
    actor_to_delete = Actor.query.filter(Actor.id == actor_id).one_or_none()

    # If no actor with given id could found, abort 404
    if not actor_to_delete:
        abort(404, {'message': 'Actor with id {} not found in database.'.format(actor_id)})
    
    # Delete actor from database
    actor_to_delete.delete()
    
    # Return json response
    return jsonify({
      'success': True,
      'deleted': actor_id
    })



#--------- Movie Endpoints -----------#


  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):

    selection = Movie.query.all()
    movies_paginated = paginate_results(request, selection)

    if len(movies_paginated) == 0:
      abort(404, {'message': 'no movies found in database.'})

    return jsonify({
      'success': True,
      'movies': movies_paginated
    })

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def insert_movies(payload):
    
    body = request.get_json()

    if not body:
          abort(400, {'message': 'request does not contain a valid JSON body.'})

    # Extract title and release_date value from request body
    title = body.get('title', None)
    release_date = body.get('release_date', None)

    # abort if one of these are missing with appropiate error message
    if not title:
      abort(422, {'message': 'no title provided.'})

    if not release_date:
      abort(422, {'message': 'no "release_date" provided.'})

    # Create new instance of movie & insert it.
    new_movie = (Movie(
          title = title, 
          release_date = release_date
          ))
    new_movie.insert()

    return jsonify({
      'success': True,
      'created': new_movie.id
    })

  @app.route('/movies/<movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movies(payload, movie_id):

    body = request.get_json()

    # Abort if no movie_id or body has been provided
    if not movie_id:
      abort(400, {'message': 'please append an movie id to the request url.'})

    if not body:
      abort(400, {'message': 'request does not contain a valid JSON body.'})

    # Find movie which should be updated by id
    movie_to_update = Movie.query.filter(Movie.id == movie_id).one_or_none()

    # Abort 404 if no movie with this id exists
    if not movie_to_update:
      abort(404, {'message': 'Movie with id {} not found in database.'.format(movie_id)})

    # Extract title and age value from request body
    title = body.get('title', movie_to_update.title)
    release_date = body.get('release_date', movie_to_update.release_date)

    # Set new field values
    movie_to_update.title = title
    movie_to_update.release_date = release_date

    # Delete movie with new values
    movie_to_update.update()

    # json response
    return jsonify({
      'success': True,
      'edited': movie_to_update.id,
      'movie' : [movie_to_update.format()]
    })

  @app.route('/movies/<movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload, movie_id):

    # Abort if no movie_id has been provided
    if not movie_id:
      abort(400, {'message': 'please append an movie id to the request url.'})
  
    # Find movie which should be deleted by id
    movie_to_delete = Movie.query.filter(Movie.id == movie_id).one_or_none()

    # If no movie with given id could found, abort 404
    if not movie_to_delete:
        abort(404, {'message': 'Movie with id {} not found in database.'.format(movie_id)})
    
    # Delete movie from database
    movie_to_delete.delete()
    
    # json response
    return jsonify({
      'success': True,
      'deleted': movie_id
    })

#--------- Error Handlers -----------#

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
            "success": False, 
            "error": 422,
            "message": get_error_message(error,"unprocessable")
            }), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
            "success": False, 
            "error": 400,
            "message": get_error_message(error, "bad request")
            }), 400

  @app.errorhandler(404)
  def ressource_not_found(error):
      return jsonify({
            "success": False, 
            "error": 404,
            "message": get_error_message(error, "resource not found")
            }), 404

  @app.errorhandler(AuthError)
  def authentification_failed(AuthError): 
      return jsonify({
            "success": False, 
            "error": AuthError.status_code,
            "message": AuthError.error['description']
            }), AuthError.status_code


#--------- returns app after every endpoint has been created -----------#

  return app

#-----------------------------------------------------------------------#

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)