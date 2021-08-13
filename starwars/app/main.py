# Import the requests library to connect to an API.
import requests
# Import the pymongo library to connect to the MongoDB database.
import pymongo

client = pymongo.MongoClient()  # Connect to MongoDB.
db = client['starwars']  # Connect to the starwars database.
db.drop_collection("starships")  # Removes any pre-existing collections named "starships".
collection = db["starships"]  # Create a new collection within the starwars database called "starships".


# Function to take an api url as a parameter, then converts the response into a json format.
def api_request(url):
    response = requests.get(url)
    return response.json()


# Function to search the character database for a specified name, and then return their object ID.
def find_character_id(name):
    return db.characters.find_one({"name": name}, {"_id": 1})


# Function to replace the pilots url in the pilot field, with the pilots object ID.
def add_pilot_id(starship_dict):
    if len(starship_dict["pilots"]) > 0:
        pilots = []
        for pilot in starship_dict["pilots"]:
            pilots.append(find_character_id(api_request(pilot)["name"]))
        starship_dict["pilots"] = pilots


# Function to create a list of all the starships that appear in any of the 4 pages of starships.
def create_starships_list():
    for page_number in range(1, 5):
        page_of_ships = api_request(f"https://swapi.dev/api/starships/?page={page_number}")["results"]
        for ship in page_of_ships:
            starships.append(ship)


starships = []  # Initialise an empty list of starships.
create_starships_list()  # Call the create_starships_list function.


for starship in starships:
    add_pilot_id(starship)
    collection.insert_one(starship)
