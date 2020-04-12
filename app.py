from flask import Flask, request, Response, jsonify
from database.db import initialize_db, host
from database.movie import Movie

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': host}
initialize_db(app)


@app.route('/movies')
def index():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype='application/json', status=200)


@app.route('/movies', methods=['POST'])
def store():
    body = request.get_json()
    movie = Movie(**body).save()
    return {'message': 'Movie was created', 'id': str(movie.id)}, 200


@app.route('/movies/<id>')
def show(id):
    movie = Movie.objects.get(id=id).to_json()
    return Response(movie, mimetype="application/json", status=200)


@app.route('/movies/<id>', methods=['PUT'])
def update(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    message = "Movie info was updated"
    return jsonify({'message': message}), 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete(id):
    Movie.objects.get(id=id).delete()
    message = "Movie record was deleted"
    return jsonify({'message': message}), 200


if __name__ == '__main__':
    app.run(debug=True)
