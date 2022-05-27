#Flask = instance; request = methods to routes; jsonify = json data
from flask import Flask, request, jsonify
import json
import sqlite3

#Creates Flask instance
app = Flask(__name__)

#################Levenshtein distance algo#####################
def loadPickle(filename):
    with open(f'{filename}', 'rb') as handle:
        loaded_pickle = pickle.load(handle)
    return loaded_pickle

all_anime_names = loadPickle('anime_names.pickle')
all_manga_names = loadPickle('manga_names.pickle')

#Get most related word
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def getMatch(name, database):
    scores = {}

    for i in database:
        scores[i] = 1 - levenshteinDistance(name, i)

    return(max(scores, key=scores.get))

################################################################


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

#Getting based on a specific parameter (ex: id, title, etc.)
@app.route('/anime/<string:name>', methods=['GET'])
def get_one_anime_byName(name):

    #Establish database connection AND connect query executioner
    connection = database_connection('anime.sqlite')
    cursor = connection.cursor()
    anime = None

    #ALGO; if name doesn't exist, replace with closest name that exists
    if name not in all_anime_names:
        new_name = getMatch(name, all_anime_names)
        name = new_name

    #Get anime based on id
    if request.method == 'GET':
        cursor.execute("SELECT * FROM anime WHERE name=?", (name,)) #SQL query
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

#Getting based on a specific parameter (ex: id, title, etc.)
@app.route('/manga/<string:name>', methods=['GET'])
def get_one_manga_byName(name):

    #Establish database connection AND connect query executioner
    connection = database_connection('manga.sqlite')
    cursor = connection.cursor()
    manga = None

    #ALGO; if name doesn't exist, replace with closest name that exists
    if name not in all_manga_names:
        new_name = getMatch(name, all_manga_names)
        name = new_name

    #Get manga based on id
    if request.method == 'GET':
        cursor.execute("SELECT * FROM manga WHERE name=?", (name,)) #SQL query
        rows = cursor.fetchall()
        for row in rows:
            manga = dict(ID = row[0], name = row[1], rating = row[2], episodes = row[3], startDate = row[4],
                 endDate = row[5], status = row[6], showType = row[7], synopsis = row[8],
                 img = row[9])

        if manga is not None:
            return jsonify(manga), 200
        else:
            return "Something went wrong", 404

#Starts the application (runs the server)
if __name__ == '__main__':
    app.run(debug=True)
