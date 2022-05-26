import requests
import pickle

#Create pickle files
def createPickle(output_name, variable):
    with open(f'{output_name}.pickle', 'wb') as handle:
        pickle.dump(variable, handle, protocol=pickle.HIGHEST_PROTOCOL)

#Testing purposes
def loadPickle(filename):
    with open(f'{filename}', 'rb') as handle:
        loaded_pickle = pickle.load(handle)
    return loaded_pickle

#Get all anime
def get_all_anime():
    all_anime = []

    for i in range(1, 14267):
        try:
            req = requests.get(f'https://kitsu.io/api/edge/anime/{i}')
            content = req.json()

            name = content['data']['attributes']['canonicalTitle']
            rating = content['data']['attributes']['averageRating']
            episodes = content['data']['attributes']['episodeCount']
            start_date = content['data']['attributes']['startDate']
            end_date = content['data']['attributes']['endDate']
            status = content['data']['attributes']['status']
            show_type = content['data']['attributes']['showType']
            synopsis = content['data']['attributes']['synopsis']
            original_img = content['data']['attributes']['posterImage']['original']

            all_anime.append([name, rating, episodes, start_date, end_date, status, show_type, synopsis, original_img])
            print(i)
        except:
            print("ERROR AT" + " " + str(i)   )
    return all_anime

#Execute anime
def executeAnime():
    all_anime = get_all_anime()
    createPickle('anime_db', all_anime)

#Get all manga
def get_all_manga():
    all_manga = []
    for i in range(1, 65000):
        try:
            req = requests.get(f'https://kitsu.io/api/edge/manga/{i}')
            content = req.json()

            name = content['data']['attributes']['canonicalTitle']

            try:
                rating = content['data']['attributes']['averageRating']
            except:
                rating = 'None'

            try:
                chapters = content['data']['attributes']['chapterCount']
            except:
                chapters = 'None'

            try:
                original_img = content['data']['attributes']['posterImage']['original']
            except:
                original_img = 'None'

            try:
                start_date = content['data']['attributes']['startDate']
            except:
                start_date = 'None'

            try:
                end_date = content['data']['attributes']['endDate']
            except:
                end_date = 'None'

            try:
                status = content['data']['attributes']['status']
            except:
                status = 'None'

            try:
                manga_type = content['data']['attributes']['mangaType']
            except:
                manga_type = 'None'

            try:
                synopsis = content['data']['attributes']['synopsis']
            except:
                synopsis = 'None'

            all_manga.append([name, rating, chapters, start_date, end_date, status, manga_type, synopsis, original_img])
            print(i)
        except:
            print("ERROR AT" + " " + str(i))

    return all_manga

#Execute manga
def executeManga():
    all_manga = get_all_manga()
    createPickle('manga_db', all_manga)

