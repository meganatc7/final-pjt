import requests
import csv
import json
from pprint import pprint

url = 'https://api.themoviedb.org/3'
key = '171c6668cf992a98b6afa81d94af7a11'
category = 'movie'
option = 'now_playing'
option2 = 'popular'
movie_lst = []
id_lst = []

# 최신 영화
for p in range(1,8):
    URL = f'{url}/{category}/{option}?api_key={key}&language=ko-KR&page={p}'
    res = requests.get(URL)
    response = res.json()

    for res in response['results']:
        id_lst.append(res['id'])


# 유명 영화
for p in range(1,35):
    URL = f'{url}/{category}/{option2}?api_key={key}&language=ko-KR&page={p}'
    res = requests.get(URL)
    response = res.json()
    for res in response['results']:
        id_lst.append(res['id'])

# kaggle영화
f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    id_lst.append(line[0])
f.close()


id_lst = list(set(id_lst))


for i in range(0,len(id_lst)):
    URL = f'{url}/{category}/{id_lst[i]}?api_key={key}&language=ko-KR'
    res = requests.get(URL)
    res = res.json()
    
    if res.get('overview') and res.get('genres'):
        tmp = {}
        tmp2 = {}
        tmp['model'] = 'movies.movie'
        tmp['pk'] = i + 1
        tmp2['title'] = res['title']
        tmp2['original_title'] = res['original_title']
        tmp2['overview'] = res['overview']
        tmp2['language'] = res['original_language']
        tmp2['poster'] = f'https://www.themoviedb.org/t/p/original/{res["poster_path"]}'
        tmp2['genres'] = ''
        genres_tmp = []
        for i in res['genres']:
            genres_tmp.append(i['name'])
        tmp2['genres'] = ' '.join(genres_tmp)
        tmp2['runtime'] = res['runtime']
        tmp2['release_date'] = res['release_date']
        tmp2['vote_average'] = res['vote_average']
        tmp2['vote_count'] = res['vote_count']
        tmp['fields'] = tmp2

        movie_lst.append(tmp)

# pprint(movie_lst)

with open('movie.json', 'w', encoding='utf-8') as w:
    json.dump(movie_lst, w, ensure_ascii=False, indent='\t')