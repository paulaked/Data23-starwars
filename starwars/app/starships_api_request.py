import requests


def starships_api_request():
    starships = []

    starships_url = "https://swapi.dev/api/starships/"

    starships_request = requests.get(starships_url)
    starships_data = starships_request.json()
    starships_results = starships_data["results"]

    starships_total_entries = starships_data["count"]

    while len(starships) < starships_total_entries:
        for i in range(0, len(starships_results)):
            starships.append(starships_results[i])
        if starships_data["next"] is not None:
            starships_url = starships_data["next"]
            starships_request = requests.get(starships_url)
            starships_data = starships_request.json()
            starships_results = starships_data["results"]
    return starships

#
# print(starships_api_request())