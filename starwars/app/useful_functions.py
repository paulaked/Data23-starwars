from collection_class import Characters


characters_col = Characters()


# this function replaces the urls in the pilots field with each pilots respective objectID
def replace_pilots(starship, starships_request):
    for index, pilot in enumerate(starship['pilots']):
        name = starships_request.pilot_name(pilot)
        object_id = characters_col.search(name)
        starship['pilots'][index] = object_id


# this function replaces the urls in the films field with each films respective objectID
def replace_films(starship, films_request, films_col):
    for index, film in enumerate(starship['films']):
        title = films_request.film_name(film)
        object_id = films_col.search(title)
        starship['films'][index] = object_id
