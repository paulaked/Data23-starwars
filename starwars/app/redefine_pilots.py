def add_obj_id(all_pages, pilot_name):
    """
    Takes all the api data and performs the final conversion to add the object ids
    :param all_pages all data sets from the api call, with names instead of urls:
    :param pilot_name a dictionary containg pilot names as keys and pilot object ids as values:
    :return all pages updatded data with object ids :
    """
    for page in all_pages:
        for ship in page:
            ship_name = str(ship["name"])
            ship["pilots"] = pilot_name[ship_name]
    return all_pages
