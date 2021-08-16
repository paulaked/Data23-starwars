import app.apiFunctions as api
import app.mongoFunctions as mb
import app.generalFunctions as gf

if __name__ == '__main__':

    ## MAIN CODE
    # Create the lists that will be used
    starships_list = []
    swapi_people_list = []
    main_people_list = []

    # Add the characters list from MongoDB
    mb.add_details_to_list(mb.characters,main_people_list,'name','_id')
    # Extract all the starships and people from Star Wars API
    api.extract_until_null('https://swapi.dev/api/starships/', starships_list)
    api.extract_until_null('https://swapi.dev/api/people/', swapi_people_list)

    # Adds characters URL to the Mongo list
    gf.add_detail_to_list(main_people_list,swapi_people_list,'url')

    # Clear collection to prevent duplicates
    mb.db.starships.delete_many({})

    # Replaces the urls in starships with object ids
    # Adds the newly appended list to the collection
    gf.append_list_and_add_to_collection(starships_list,main_people_list,mb.db.starships)

