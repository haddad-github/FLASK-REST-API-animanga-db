# REST API for Anime and Manga

### This repository contains all the files that were used to create the API; a private repository is used as the host for Heroku

#### Accessing the entire database:
https://animanga-db.herokuapp.com/anime/

https://animanga-db.herokuapp.com/manga/

#### Currently takes int ID's, such as:
https://animanga-db.herokuapp.com/anime/852

https://animanga-db.herokuapp.com/manga/57382

For anime, returns:
_'unique ID', 'name', 'rating', 'episodes', 'startDate', 'endDate', 'status', 'showType', 'synopsis', 'img'_

For manga, returns:
_'unique ID', 'name', 'rating', 'chapters', 'start_date', 'end_date', 'status', 'manga_type', 'synopsis', 'original_img'_

Image showing an anime request:
![image](https://user-images.githubusercontent.com/68672661/170551817-d550549e-7e36-4b6a-a6e9-1f0e6a316ee1.png)
