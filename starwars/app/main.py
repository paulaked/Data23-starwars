import starship_api as sa
import pymongo
from pprint import pprint as pp

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['starwars']
col = db["starships"]

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
y = len(list_starships)
z = len(pilot_name)
for starship in range(y):
    ship = list_starships[starship]['pilots']
    # pp(ship)
    for s in ship:
        ship_pilot_check = sa.api_call(s)
        ship_pilot_name = sa.api_api(s)
        # print(ship_pilot_name)  # so here we have used the pilot url in starship data to get the data from the api
        pilot_name_url1 = list(pilot_name_url)
        pilot_name_url1.append(ship_pilot_name)
        pilot_name_url = tuple(pilot_name_url1)
# print(pilot_name_url)
id_and_name = []
n = len(pilot_name_url)
for x in range(n):
    name_of_pilot = pilot_name_url[x]['name']
    for name in name_of_pilot:
        get_name = sa.mongdb_name_id(name_of_pilot)
        id_and_name.append(get_name)
print(id_and_name) # so now we have the object ids


for x in range(n):
    name_of_pilot = pilot_name_url[x]['name']
    url_of_pilot = pilot_name_url[x]['url']
    for starship in range(y):
        ship = list_starships[starship]['pilots']
        if url_of_pilot in ship:
            pp(ship)
            pp(url_of_pilot) # we can see that id and url are there :)





