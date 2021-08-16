import pymongo

client = pymongo.MongoClient()
db = client['starwars']
character_list = []
characters = db.characters.find({})


# Loops through a collection and appends the details to a list
def add_details_to_list(objects, storage, detail1, detail2):
   for i in objects:
       storage.append([i[detail1], [i[detail2]]])

