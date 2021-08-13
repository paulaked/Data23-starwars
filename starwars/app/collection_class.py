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

    def access(self):
        content = {}
        for item in self.db.characters.find({}):
            content[item['name']] = item
        return content


class Starships(Collection):

    def __init__(self):
        super().__init__()
        self.name = "starships"
        self.size = self.db.starships.estimated_document_count()
        self.content = self.access()

    def access(self):
        content = {}
        for item in self.db.starships.find({}):
            content[item['name']] = item
        return content

    def clear(self):
        self.db.starships.delete_many({})

