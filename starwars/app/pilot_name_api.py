def pilot_name_dict(all_pages):
    from app.init_mongodb import mongo_setup
    db = mongo_setup()
    import requests
    ship_pilot_dict = {}
    for page in all_pages:
        for ship in page:
            pilots_in_ship = []
            pilots = ship["pilots"]
            ship_name = str((ship['name']))
            for pilot_url in pilots:
                pilot = (str(requests.get(pilot_url).json()['name']))
                object_name = db.characters.find_one({"name": pilot}, {"_id": 1})
                pilots_in_ship.append(object_name)
            update_dict = {ship_name: pilots_in_ship}
            ship_pilot_dict.update(update_dict)
    return ship_pilot_dict
