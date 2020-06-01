MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movies():
    
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie_name in movies:
        print(movie_name)

def find_movies():
    find_movie_prompt = input("Enter movie name you're looking for: ")
    
    for movie_name in movies:  
        if movie_name['title'] == find_movie_prompt:
            print(movie_name)

user_selection = {
    "a": add_movies,
    "l": list_movies,
    "f": find_movies
    } 
    

def user_menu():
        
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_selection:
            selected_function = user_selection[selection]
            selected_function()
      
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

user_menu()
