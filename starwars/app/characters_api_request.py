import requests  # Allows for the importing of data from the api


def characters_api_request():
    characters = []

    characters_url = "https://swapi.dev/api/people/"

    characters_request = requests.get(characters_url)
    characters_data = characters_request.json()
    characters_results = characters_data["results"]

    characters_total_entries = characters_data["count"]

    while len(characters) < characters_total_entries:
        for i in range(0, len(characters_results)):
            characters.append(characters_results[i])
        if characters_data["next"] is not None:
            characters_url = characters_data["next"]
            characters_request = requests.get(characters_url)
            characters_data = characters_request.json()
            characters_results = characters_data["results"]
    return characters
