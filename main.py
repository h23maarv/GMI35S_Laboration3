import requests
import modules
import config

menu = 0
while menu != 4:
    try:
        menu = int(input
            ("\n-------------------------------------------"
            "\n1. Sök efter en film baserat på exakt titel"
            "\n2. Sök efter en film baserat på något ord i filmens titel"
            "\n3. Historik"
            "\n4. Avsluta programmet."
            "\n-------------------------------------------\n"))
        match menu:
            case 1: #Search for a movie with exact word
                movie_title = input("Vilken film vill du söka efter?:\n")
                modules.Search_for_movie(movie_title)
            case 2: #Search for a movie with a word
                modules.Search_for_movie_one_word(movie_title)
                movie_title = input("Vilken film vill du söka efter?:\n")
            case 3: #History
                modules.history()
            case 4: #Stäng av programmet
                pass
            case default:
                print("Ej giltig input, testa ett heltal.\n")
    except ValueError:
        print("Ej giltig input, testa ett heltal.\n")