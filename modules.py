import requests
import json
import config

API_KEY = config.api_key


def Search_for_movie(movie_title):
    try:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            print("\n", response.status_code)
            movie_title = response.json()

            for key in movie_title:
                print("\n", key, ":", movie_title[key])
            try:
                with open('file.json', 'w', encoding = 'utf-8-sig') as fpointer:
                    json.dump(movie_title, fpointer, indent = 4, ensure_ascii = False)
            except FileNotFoundError as err:
                print("\n", err)

        else:
            print(f"Error: {movie_title.status_code}")
    except requests.exceptions.HTTPError as ferr:
        print("\nnot found")
        print("\n", ferr)


def Search_for_movie_one_word(whole_movie_title):
    try:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={whole_movie_title}"
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            print("\n", response.status_code)
            whole_movie_title = response.json()

            for movie in whole_movie_title["Search"]:
                for key, value in movie.items():
                    print("\n", key, ":", value)

            try:
                with open('file.json', 'w', encoding='utf-8-sig') as fpointer:
                    json.dump(whole_movie_title, fpointer, indent = 4, ensure_ascii = False)
            except FileNotFoundError as err:
                print(err)

        else:
            print(f"Error: {whole_movie_title.status_code}")
    except requests.exceptions.HTTPError as ferr:
        print("\nnot found")
        print("\n", ferr)


def Last_searched_movie():
    while True:
        try:
            with open("file.json", "r", encoding = "utf-8-sig") as fpointer:
                movies = json.load(fpointer)

                if "Search" in movies:
                    for movie in movies["Search"]:
                        for key, value in movie.items():
                            print("\n", key, ":", value)
                else:
                    for key in movies:
                        print("\n", key, ":", movies[key])
                print("\nAll data i JSON-filen är utskriven.")
                break
        except FileNotFoundError:
            print("\nFilen kunde inte hittas.")
            break


def Userhistory():
    while True:
        try:
            with open("user_input.txt", "r", encoding = "utf-8-sig") as file:
                content = file.read()
                print(content)

            print("\nAlla sökord är utskrivna.")
            break
        except FileNotFoundError:
            print("\nFilen kunde inte hittas.")
            break