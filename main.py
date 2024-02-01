import modules
menu = 0
while menu != 5:
    try:
        menu = int(input
            ("\n-------------------------------------------"
            "\n1. Sök efter en film baserat på exakt titel"
            "\n2. Sök efter en film baserat på något ord i filmens titel"
            "\n3. Senaste sökta film(erna)"
            "\n4. Skriv ut sökordhistoriken"
            "\n5. Avsluta programmet."
            "\n-------------------------------------------\n"))
        match menu:
            case 1: #Search for a movie with exact word
                movie_title = input("\nVilken film vill du söka efter?:\n")
                with open("user_input.txt", "a", newline = "") as file:
                    file.write(movie_title + "\n")
                modules.Search_for_movie(movie_title)
            case 2: #Search for a movie with a word
                whole_movie_title = input("\nVilken film vill du söka efter?:\n")
                with open("user_input.txt", "a", newline = "") as file:
                    file.write(whole_movie_title + "\n")
                modules.Search_for_movie_one_word(whole_movie_title)
            case 3: #Last searched movie history
                modules.Last_searched_movie()
            case 4: #Userhistory
                modules.Userhistory()
            case 5: #Stäng av programmet
                pass
            case default:
                print("Ej giltig input, testa ett heltal.\n")
    except ValueError:
        print("Ej giltig input, testa ett heltal.\n")