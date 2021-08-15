from API_class import Api
from collection_class import *
from useful_functions import *


if __name__ == '__main__':
    # instantiating all the classes
    starships_request = Api("https://swapi.dev/api/starships/")
    films_request = Api("https://swapi.dev/api/films/")
    starships_col = Starships()
    films_col = Films()

    # pull all data about starships
    starships = starships_request.results()

    # clear the original starships and films collections in MongoDB
    starships_col.clear()
    films_col.clear()

    # insert the relevant films data into the films collection in MongoDB
    films = films_request.transform_films()
    for film in films:
        films_col.insert(film)

    # for each starship, replace the pilots field with a list of objectIDs
    # also, replace the films field with a list of objectIDs
    # then insert the data of each starship into the starships collection in MongoDB
    for ship in starships:
        replace_pilots(ship, starships_request)
        replace_films(ship, films_request, films_col)
        starships_col.insert(ship)
