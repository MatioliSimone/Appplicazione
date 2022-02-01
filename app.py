import json
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

def getImageSrc(image):
    return IMAGES_PATH + "/" + image

def filterMovie(movie):
    if "poster" in movies.keys():
        movie["poster"] = getImageSrc(movie["director_avatar"])
    if "director_avatar" in movies.keys():
        movie["director_avatar"] = getImageSrc(movie["director_avatar"])
    return movie  
          
def hello():
     return jsonify(movies)

@app.route('/movies', methods=['POST'])

def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return jsonify, 200

app.run()