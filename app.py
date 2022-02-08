from flask_cors import CORS
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

IMAGES_PATH = "/static/img"
POSTER_FORMAT_NAME = "{}_Poster.jpg"

def getImageSrc(image):
    return IMAGES_PATH+"/"+image

def filterMovie(movie):
    if "poster" in movie.keys():
        movie["poster"] = getImageSrc(movie["poster"])
    if "director_avatar" in movie.keys():
        movie["director_avatar"] = getImageSrc(movie["director_avatar"])
    return movie

def filterMovies(movies):
    return [ filterMovie(m.copy()) for m in movies]

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200   
 
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200

@app.route('/movies', methods=['POST'])
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200

app.run()