from app.api import api_call
from app.init_mongodb import mongo_setup
from app.pilot_name_api import pilot_name_dict
from app.redifine_pilots import add_obj_id

all_pages = api_call()
db = mongo_setup()
ship_pilot_dict = pilot_name_dict(all_pages)
all_pages = add_obj_id(all_pages,ship_pilot_dict)
for page in all_pages:
    db.starship.insert_many(page)