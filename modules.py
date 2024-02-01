import requests
import json
import config

API_KEY = config.api_key

def Search_for_movie(movie_title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        print(response.status_code)
        content_text = response.text
        print(content_text)
        movie_title = response.json().get('movies', [])
        print(movie_title)

        with open('file.json', 'w', encoding='utf-8-sig') as fpointer:
                    json.dump(movie_title, fpointer, indent = 4, ensure_ascii = False)

    else:
        print(f"Error: {movie_title.status_code}")

Search_for_movie("")

def jprint(obj):
    print(json.dumps(obj, sort_keys = True, indent = 4, ensure_ascii = False))

def Search_for_movie_one_word(movie_title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={movie_title}"
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        print(response.status_code)
        content_text = response.text
        print(content_text)
        serched_movie = response.json().get('movies', [])
        print(serched_movie)

        with open('file.json', 'w', encoding='utf-8-sig') as fpointer:
                    json.dump(serched_movie, fpointer, indent = 4, ensure_ascii = False)

    else:
        print(f"Error: {serched_movie.status_code}")

Search_for_movie_one_word("")

def jprint(obj):
    print(json.dumps(obj, sort_keys = True, indent = 4, ensure_ascii = False))

def history():
    while True:
        try:
            with open("file.json", "r", encoding = "utf-8-sig") as jsonfile:
                movies = json.load(jsonfile)

                for key in movies:
                    print("\n", key, ":", movies[key])
                print("\nAll data i JSON-filen är utskriven.")
                break
        except FileNotFoundError:
            print("\nFilen kunde inte hittas.")
            break