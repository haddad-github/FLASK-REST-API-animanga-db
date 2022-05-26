import pandas
import sqlite3

###ANIME###
#ID, name, rating, episodes, start_date, end_date, status, show_type, synopsis, original_img

#Connect sqlit3 to database (if doesn't exist, it will be created)
connection = sqlite3.connect('anime.sqlite')

#Links commands to the database
cursor = connection.cursor()

#Make the sql_query to create the database
sql_query = """ CREATE TABLE anime (
    ID integer NOT NULL PRIMARY KEY,
    name text,
    rating float,
    episodes integer,
    startDate date,
    endDate date,
    status text,
    showType text,
    synopsis text,
    img text
)"""

#Execute the SQL query above to create database
cursor.execute(sql_query)

#Reads csv
df = pandas.read_csv('anime.csv')
df.columns = ['ID', 'name', 'rating', 'episodes', 'startDate', 'endDate', 'status', 'showType', 'synopsis', 'img']
df.to_sql('anime', connection, if_exists='append', index=False)


###ANIME###



###MANGA###
#ID, name, rating, chapters, start_date, end_date, status, manga_type, synopsis, original_img

#Connect sqlit3 to database (if doesn't exist, it will be created)
connection2 = sqlite3.connect('manga.sqlite')

#Links commands to the database
cursor2 = connection2.cursor()

#Make the sql_query to create the database
sql_query = """ CREATE TABLE manga (
    ID integer NOT NULL PRIMARY KEY,
    name text,
    rating float,
    chapters integer,
    startDate date,
    endDate date,
    status text,
    mangaType text,
    synopsis text,
    img text
)"""

#Execute the SQL query above to create database
cursor2.execute(sql_query)

#Reads csv
df2 = pandas.read_csv('manga.csv')
df2.columns = ['ID', 'name', 'rating', 'chapters', 'startDate', 'endDate', 'status', 'mangaType', 'synopsis', 'img']
df2.to_sql('manga', connection2, if_exists='append', index=False)

###MANGA###