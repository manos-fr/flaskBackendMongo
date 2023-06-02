from bson import json_util
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


app.config["MONGO_URI"] = "mongodb://localhost:27017/movies"
mongo = PyMongo(app)


@app.route('/titles', methods=['GET'])
def get_titles():
    try:
        titles = [titles for titles in mongo.db.titles.find()]
        titlesStr = json.dumps(titles, default=json_util.default)
        return {'rows': json.loads(titlesStr)}
    except:
        return {'error'}



@app.route('/titles/<id>', methods=['GET'])
def get_titleById(id):
    title = [title for title in mongo.db.titles.find({'tconst': id})]
    titlesStr = json.dumps(title, default=json_util.default)
    return {'rows': json.loads(titlesStr)}


@app.route('/titles', methods=['POST'])
def create_title():
    body: dict = request.get_json()
    mongo.db.titles.insert_one(
        {'tconst': f"{body.get('tconst')}", 'originalTitle': f"{body.get('originalTitle')}", 'startYear': f"{body.get('startYear')}", 'genres': f"{body.get('genres')}"})
    return {'tconst': f"{body.get('tconst')}", 'originaTitle': f"{body.get('originalTitle')}", 'startYear': f"{body.get('startYear')}", 'genres': f"{body.get('genres')}"}


@app.route('/titles/<id>', methods=['PUT'])
def update_title(id):
    body: dict = request.get_json()
    mongo.db.titles.update_one(
        {'tconst': id}, {"$set": {'genres': body.get('genres'), 'startYear': body.get('startYear'), 'originalTitle': body.get('originalTitle')}}, upsert=True)
    return {'genres': body.get('genres'), 'startYear': body.get('startYear'), 'originalTitle': body.get('originalTitle')}


@app.route('/titles/<id>', methods=['DELETE'])
def delete_titleId(id):
    mongo.db.titles.delete_one({'tconst': id})
    return {'res': f"Deleted title with id: {id}"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)
