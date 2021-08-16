import pymongo

client = pymongo.MongoClient()
db = client['starwars']
character_list = []
characters = db.characters.find({})


def add_to_list(objects, storage):
   for i in objects:
       storage.append([i['name'], [i['_id']]])

# add_to_list(characters, character_list)
# # print(len(character_list))
# # print(character_list[0])
