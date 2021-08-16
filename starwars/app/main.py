import starship_api as sa
import pymongo
from pprint import pprint as pp

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['starwars']
col = db["starships"]

sa.clear_starships()

list_starships = []
stsh = sa.api_call("https://swapi.dev/api/starships")
starship_response = sa.crawl_api("https://swapi.dev/api/starships")
for result in starship_response:
    list_starships.append(result)
    col.insert_one(result)



pilot_name = []
pilot = sa.api_call("https://swapi.dev/api/people")
pilot_response = sa.crawl_api("https://swapi.dev/api/people")
for result in pilot_response:
    pilot_name.append(result)
# pp(pilot_name)
pilot_name_url = ()
new_list = []
id_and_name = []
z = len(pilot_name)
for starship in range(0, len(list_starships)):
    ship = list_starships[starship]['pilots']
    # pp(ship)
    for s in ship:
        ship_pilot_check = sa.api_call(s)
        ship_pilot_name = sa.api_api(s)
        # print(ship_pilot_name)  # so here we have used the pilot url in starship data to get the data from the api
        pilot_name_url1 = list(pilot_name_url)
        pilot_name_url1.append(ship_pilot_name)
        pilot_name_url = tuple(pilot_name_url1)
        # get_name = sa.mongdb_name_id(s)
        # id_and_name.append(get_name)
        # new_list.append(id_and_name)
# pp(new_list)
# print(pilot_name_url)

for index, starship in enumerate(list_starships):  # get index as index and starship is all the info
    for index2, url in enumerate(starship['pilots']):
        get_name = sa.mongo_api_url(url)
        get_name_and_id = sa.mongdb_name_id(get_name)
        id_and_name.append(get_name_and_id)
        # pp(id_and_name)  # this gives us name and id for each ships specifically
        starship['pilots'][index2] = get_name_and_id['_id']

# pp(starship)
# pp(list_starships)

sa.clear_starships()
for starship in list_starships:
    col.insert_one(starship)


# id_and_name = []
# for x in range(0, len(pilot_name_url)):
#     name_of_pilot = pilot_name_url[x]['name']
#     for name in name_of_pilot:
#         get_name = sa.mongdb_name_id(name_of_pilot)
#         id_and_name.append(get_name)
#
# new_list = []
# id_name = []
# for x in range(0, len(pilot_name_url)):
#     name_of_pilot = pilot_name_url[x]['name']
#     for name in name_of_pilot:
#         get_name = sa.mongdb_name_id(name_of_pilot)
#         id_and_name.append(get_name)
#         new_list.append(get_name)

# print(id_and_name) # so now we have the object ids

# new_ship_list = []
# for x in range(0, len(pilot_name_url)):
#     name_of_pilot = pilot_name_url[x]['name']
#     url_of_pilot = pilot_name_url[x]['url']
#     for starship in range(0, len(list_starships)):
#         ship = list_starships[starship]
#         if url_of_pilot in ship:
#             # list_starships[starship]['pilots'] = name_of_pilot #this does not work and gives last name to it
#             # list_starships[starship]['pilots'] = 0 # this makes all pilots 0
#             new_ship_list.append(ship)
#             # pp(list_starships)
#             # pp(ship)
#             # pp(url_of_pilot) # we can see that id and url are there :)
#             pp(new_ship_list)

# pp(list_starships)  #all 36 starships
# pp(pilot_name_url)  # opens people link for all the pilots in each starship
# pp(id_and_name)  # object_id + name

# for name in pilot_name_url:
#     if name['name']




