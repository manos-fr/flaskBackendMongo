import psycopg2
from psycopg2 import Error
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/titles', methods=['GET'])
def get_titles():
    try:
        cursor = connection.cursor()
        with connection:
            cursor.execute(f"SELECT * FROM titles")
            response = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    key_list = ["tconst", "titletype", "originaltitle", "primarytitle",
                "isadult", "startyear", "endyear", "runtimeminutes", "genres"]

    res = []

    for i in range(0, len(response)-1):
        res.append({
            key_list[0]: response[i][0],
            key_list[1]: response[i][1],
            key_list[2]: response[i][2],
            key_list[3]: response[i][3],
            key_list[4]: response[i][4],
            key_list[5]: response[i][5],
            key_list[6]: response[i][6],
            key_list[7]: response[i][7],
            key_list[8]: response[i][8],
        })
    return {'rows': res}


@app.route('/titles/<id>', methods=['GET'])
def get_titleById(id):
    try:
        cursor = connection.cursor()
        with connection:
            print(id)
            cursor.execute(
                f"SELECT * FROM titles WHERE tconst = '{id}' ORDER BY startyear ASC")
            response = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    key_list = ["tconst", "titletype", "originaltitle", "primarytitle",
                "isadult", "startyear", "endyear", "runtimeminutes", "genres"]

    res = {
        key_list[0]: response[0][0],
        key_list[1]: response[0][1],
        key_list[2]: response[0][2],
        key_list[3]: response[0][3],
        key_list[4]: response[0][4],
        key_list[5]: response[0][5],
        key_list[6]: response[0][6],
        key_list[7]: response[0][7],
        key_list[8]: response[0][8],
    }
    return {'rows': [res]}


@app.route('/titles/<id>', methods=['DELETE'])
def delete_titleById(id):
    try:
        cursor = connection.cursor()
        with connection:
            print(id)
            cursor.execute(
                f"DELETE FROM titles WHERE tconst = '{id}'")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return {'message': f"Deleted title with id: {id}"}


@app.route('/titles', methods=['POST'])
def create_title():
    try:
        cursor = connection.cursor()
        with connection:
            data: dict = request.get_json()
            print(data)
            cursor.execute(
                f"INSERT INTO titles (tconst, originaltitle, startyear, genres) VALUES ('{data.get('tconst')}', '{data.get('originalTitle')}', {data.get('startYear')}, '{data.get('genres')}') RETURNING *")
            response = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    key_list = ["tconst", "titletype", "originaltitle", "primarytitle",
                "isadult", "startyear", "endyear", "runtimeminutes", "genres"]

    res = []

    for i in range(0, len(response)-1):
        res.append({
            key_list[0]: response[i][0],
            key_list[1]: response[i][1],
            key_list[2]: response[i][2],
            key_list[3]: response[i][3],
            key_list[4]: response[i][4],
            key_list[5]: response[i][5],
            key_list[6]: response[i][6],
            key_list[7]: response[i][7],
            key_list[8]: response[i][8],
        })
    return {'rows': res}


@app.route('/titles/<id>', methods=['PUT'])
def update_title(id):
    try:
        cursor = connection.cursor()
        with connection:
            data: dict = request.get_json()
            print(data)
            cursor.execute(
                f"UPDATE titles SET originaltitle= '{data.get('originalTitle')}', startyear= {data.get('startYear')}, genres= '{data.get('genres')}' WHERE tconst = '{id}'")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return {'message': f"Updated title with id: {id}"}


if __name__ == '__main__':
    connection = psycopg2.connect(user="vqlnioqfkvocxj", password="20de6fb3a0fd8e652444adbe7273c89429f28c11cc1376e46eb789cfb8474bef",
                                  host="ec2-54-229-217-195.eu-west-1.compute.amazonaws.com", port="5432", database="de9mikemijit5j")
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)
