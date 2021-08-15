import pymongo


class Collection:

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['starwars']


class Characters(Collection):

    def __init__(self):
        super().__init__()
        self.name = "characters"
        self.size = self.db.characters.estimated_document_count()
        self.content = self.access()

    # this accesses the characters data and stores it in a dictionary with keys being the characters name
    def access(self):
        content = {}
        for item in self.db.characters.find({}):
            content[item['name']] = item
        return content

    # this takes in a characters name and returns their objectID in the characters collection in MongoDB
    def search(self, name: str):
        query = self.db.characters.find_one({'name': name}, {'_id': 1})
        return query['_id']


class Starships(Collection):

    def __init__(self):
        super().__init__()
        self.name = "starships"
        self.size = self.db.starships.estimated_document_count()
        self.content = self.access()

    # this accesses the starships data and stores it in a dictionary with keys being the starships name
    def access(self):
        content = {}
        for item in self.db.starships.find({}):
            content[item['name']] = item
        return content

    # this deletes all documents from the starships collection
    def clear(self):
        self.db.starships.delete_many({})
        self.size = self.db.starships.estimated_document_count()

    # this takes a characters name and returns their document details
    def search(self, name: str):
        return self.db.starships.find_one({'name': name})

    # this inserts a document into the starships collection
    def insert(self, document: dict):
        self.db.starships.insert_one(document)
        self.size = self.db.starships.estimated_document_count()


class Films(Collection):

    def __init__(self):
        super().__init__()
        self.name = "films"
        self.size = self.db.films.estimated_document_count()

    # this inserts a document into the films collection
    def insert(self, document: dict):
        self.db.films.insert_one(document)
        self.size = self.db.films.estimated_document_count()

    # this deletes all documents from the films collection
    def clear(self):
        self.db.films.delete_many({})
        self.size = self.db.films.estimated_document_count()

    # this takes a film name and returns their objectID in the films collection in MongoDB
    def search(self, title: str):
        query = self.db.films.find_one({'title': title}, {'_id': 1})
        return query['_id']

    # this takes a films title and returns its document details
    def search_details(self, title: str):
        return self.db.films.find_one({'title': title})
