MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

GetTitle = lambda : input("Enter the movie title: ")
GetDirector = lambda : input("Enter the movie director: ")
GetYear = lambda : input("Enter the movie release year: ")
FindThisMovieTitle = lambda : input("Title: ")

movies = {}
title = GetTitle()
movies[title] = Movie(title, GetDirector(), GetYear())

PrintLine = lambda movie : print(f"Movie: {movie.title}, Year: {movie.year}, Director: {movie.director}")

def PrintMovies():
    for movie in movies.values():
        PrintLine(movie)


def FindMovie():
    title = FindThisMovieTitle()
    movie_found = movies.get(title)
    if(movie_found):
        PrintLine(movie_found)
    else:
        print("None found")


def AddMovie():
    title = GetTitle()
    director = GetDirector()
    year = GetYear()
    new_movie = Movie(title, director, year)
    movies[title] = new_movie

user_options = {
    "a": AddMovie,
    "l": PrintMovies,
    "f": FindMovie
}

def Main():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection in user_options:
            selected_action = user_options[selection]
            selected_action()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

Main()