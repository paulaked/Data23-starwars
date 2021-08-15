def mongo_setup():
    import pymongo
    """
    Connects python to the mongo database, and clears existing collections
    """
    client = pymongo.MongoClient()
    db = client['starwars']
    db.starships.drop()
    return db