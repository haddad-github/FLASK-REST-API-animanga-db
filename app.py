#Flask = instance; request = methods to routes; jsonify = json data
from flask import Flask, request, jsonify
import json
import sqlite3

#Creates Flask instance
app = Flask(__name__)

#Data loaded from sqlite file
def database_connection(sqlite_database):
    connection = None
    try:
        connection = sqlite3.connect(sqlite_database)
    except sqlite3.error as e:
        print(e)
    return connection

####ANIME####

#GET anime
@app.route('/anime/', methods=['GET'])
def anime():

    #Establish database connection AND connect query executioner
    connection = database_connection('anime.sqlite')
    cursor = connection.cursor()

    if request.method == 'GET':

        #Getter SQL query
        cursor = connection.execute("SELECT * FROM anime") #SQL query

        #Transform csv into dictionary with keys for each data
        #['ID', 'name', 'rating', 'episodes', 'startDate', 'endDate', 'status', 'showType', 'synopsis', 'img']
        anime_list = [

            dict(ID = row[0], name = row[1], rating = row[2], episodes = row[3], startDate = row[4],
                 endDate = row[5], status = row[6], showType = row[7], synopsis = row[8],
                 img = row[9])

            for row in cursor.fetchall() #get all
        ]

        if anime_list is not None:
            return jsonify(anime_list)

#Getting based on a specific parameter (ex: id, title, etc.)
@app.route('/anime/<int:ID>', methods=['GET'])
def get_one_anime(ID):

    #Establish database connection AND connect query executioner
    connection = database_connection('anime.sqlite')
    cursor = connection.cursor()
    anime = None

    #Get anime based on id
    if request.method == 'GET':
        cursor.execute("SELECT * FROM anime WHERE ID=?", (ID,)) #SQL query
        rows = cursor.fetchall()
        for row in rows:
            anime = dict(ID = row[0], name = row[1], rating = row[2], episodes = row[3], startDate = row[4],
                 endDate = row[5], status = row[6], showType = row[7], synopsis = row[8],
                 img = row[9])

        if anime is not None:
            return jsonify(anime), 200
        else:
            return "Something went wrong", 404


####MANGA####
#GET manga
@app.route('/manga/', methods=['GET'])
def manga():

    #Establish database connection AND connect query executioner
    connection = database_connection('manga.sqlite')
    cursor = connection.cursor()

    if request.method == 'GET':

        #Getter SQL query
        cursor = connection.execute("SELECT * FROM manga") #SQL query

        #Transform csv into dictionary with keys for each data
        #[ID, name, rating, chapters, start_date, end_date, status, manga_type, synopsis, original_img]
        manga_list = [

            dict(ID = row[0], name = row[1], rating = row[2], chapters = row[3], startDate = row[4],
                 endDate = row[5], status = row[6], mangaType = row[7], synopsis = row[8],
                 img = row[9])

            for row in cursor.fetchall() #get all
        ]

        if manga_list is not None:
            return jsonify(manga_list)

#Getting based on a specific parameter (ex: id, title, etc.)
@app.route('/manga/<int:ID>', methods=['GET'])
def get_one_manga(ID):

    #Establish database connection AND connect query executioner
    connection = database_connection('manga.sqlite')
    cursor = connection.cursor()
    manga = None

    #Get manga based on id
    if request.method == 'GET':
        cursor.execute("SELECT * FROM manga WHERE ID=?", (ID,)) #SQL query
        rows = cursor.fetchall()
        for row in rows:
            manga = dict(ID = row[0], name = row[1], rating = row[2], chapters = row[3], startDate = row[4],
                 endDate = row[5], status = row[6], mangaType = row[7], synopsis = row[8],
                 img = row[9])

        if manga is not None:
            return jsonify(manga), 200
        else:
            return "Something went wrong", 404


#Starts the application (runs the server)
if __name__ == '__main__':
    app.run(debug=True)
