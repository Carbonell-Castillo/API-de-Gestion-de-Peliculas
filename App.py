from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

movies_db = {}

# Endpoint para agregar una película
@app.route('/api/new-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie_id = data.get("movieId")
    name = data.get("name")
    genre = data.get("genre")

    if movie_id is not None and name is not None and genre is not None:
        movies_db[movie_id] = {"name": name, "genre": genre}
        return jsonify({"message": f"Película '{name}' agregada con éxito."}), 201
    else:
        return jsonify({"error": "Faltan datos en la solicitud."}), 400

# Endpoint para obtener todas las películas por género
@app.route('/api/all-movies-by-genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    genre = genre.capitalize()
    movies = [movie for movie in movies_db.values() if movie["genre"] == genre]
    return jsonify(movies), 200

# Endpoint para actualizar una película
@app.route('/api/update-movie', methods=['PUT'])
def update_movie():
    data = request.get_json()
    movie_id = data.get("movieId")
    name = data.get("name")
    genre = data.get("genre")

    if movie_id in movies_db:
        if name is not None:
            movies_db[movie_id]["name"] = name
        if genre is not None:
            movies_db[movie_id]["genre"] = genre
        return jsonify({"message": f"Película con ID {movie_id} actualizada con éxito."}), 200
    else:
        return jsonify({"error": f"No se encontró una película con ID {movie_id}."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
