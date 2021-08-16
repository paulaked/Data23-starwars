def mongo_setup():
    """
    Connects python to the mongo database, and clears any existing starship collection
    :return the database client as db
    """
    import pymongo
    client = pymongo.MongoClient()
    db = client['starwars']
    db.starship.drop()
    return db