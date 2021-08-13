from API_class import Api
from collection_class import Starships
from useful_functions import replace


if __name__ == '__main__':
    # instantiating all the classes
    starships_request = Api("https://swapi.dev/api/starships/")
    starships_col = Starships()

    # pull all data about starships
    starships = starships_request.results()

    # clear the original starships collection in MongoDB
    starships_col.clear()

    # in each starship, replace the pilots field with a list of objectIDs
    # then insert the data of each starship into the starships collection in MongoDB
    for ship in starships:
        replace(ship, starships_request)
        starships_col.insert(ship)
