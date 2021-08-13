from collection_class import Characters


characters_col = Characters()


# this function replaces the urls in the pilots field with each pilots respective objectID
def replace(starship, starships_request):
    for index, pilot in enumerate(starship['pilots']):
        name = starships_request.pilot_name(pilot)
        object_id = characters_col.search(name)
        starship['pilots'][index] = object_id
