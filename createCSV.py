import csv
import pickle
import pandas as pd

#Load databases
def loadPickle(filename):
    with open(f'{filename}', 'rb') as handle:
        loaded_pickle = pickle.load(handle)
    return loaded_pickle

#Write them to CSV
def writeToCSV(data, csv_output):
    with open(csv_output, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

#Read the CSV for testing purposes
def readCSV(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

#Add ID column (without header)
def add_ID_to_CSV(csv_file):
    pd.read_csv(csv_file, header = None).to_csv(csv_file, header = False)

# anime_db = loadPickle('anime_db.pickle')
# manga_db = loadPickle('manga_db.pickle')
#
# writeToCSV(anime_db, 'anime.csv')
# writeToCSV(manga_db, 'manga.csv')
#
# readCSV('anime.csv')
# readCSV('manga.csv')
#
# add_ID_to_CSV('anime.csv')
# add_ID_to_CSV('manga.csv')