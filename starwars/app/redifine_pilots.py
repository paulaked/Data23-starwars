def add_obj_id(all_pages, pilot_name):
    for page in all_pages:
        for ship in page:
            ship_name = str(ship["name"])
            ship["pilots"] = pilot_name[ship_name]
    return all_pages
