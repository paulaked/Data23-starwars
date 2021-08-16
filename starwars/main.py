from app.api import api_call
from app.init_mongodb import mongo_setup
from app.pilot_name_api import pilot_name_dict
from app.redefine_pilots import add_obj_id
# imports all relative document

all_pages = api_call()
# extract all starship data in json format with pages
db = mongo_setup()
# initialises mongo database
ship_pilot_dict = pilot_name_dict(all_pages)
# returns dictionary of ship name and pilot name
all_pages = add_obj_id(all_pages,ship_pilot_dict)
# adds object ids to the complete set of data
for page in all_pages:
    db.starship.insert_many(page)