import app.apiFunctions as api
import app.mongoFunctions as mb
from pprint import pprint
import requests

if __name__ == '__main__':
    ## MAIN CODE
    starships_list = []
    swapi_people_list = []
    main_people_list = []

    mb.add_to_list(mb.characters,main_people_list)
    api.extract_until_null('https://swapi.dev/api/starships/', starships_list)
    api.extract_until_null('https://swapi.dev/api/people/', swapi_people_list)


    # Adds characters URL to the Mongo list
    for i in range(len(main_people_list)):
        for j in range(len(swapi_people_list)):
            if main_people_list[i][0] == swapi_people_list[j]['name']:
                main_people_list[i][1].append(swapi_people_list[j]['url'])
        if len(main_people_list[i][1]) == 1:
            main_people_list[i][1].append('No record')

    mb.db.starships.delete_many({})

    # replaces the urls in starships with object ids
    for i in range(len(starships_list)):
        for j in range(len(starships_list[i]['pilots'])):
            name = None

            for k in range(len(main_people_list)):
                if starships_list[i]['pilots'][j] == main_people_list[k][1][1]:
                    starships_list[i]['pilots'].pop(j)
                    name = main_people_list[k][0]
                    starships_list[i]['pilots'].append(main_people_list[k][1][0])
        mb.db.starships.insert_one(starships_list[i])

