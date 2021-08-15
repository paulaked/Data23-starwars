import requests

def api_call():
    response = []
    call = requests.get("https://swapi.dev/api/starships")
    response.append(call.json()["results"])
    next_url = call.json()["next"]
    while str(next_url) != "None":
        call = requests.get(next_url)
        next_url = call.json()["next"]
        response.append(call.json()["results"])
    return response






