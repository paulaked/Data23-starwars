import requests
def api_request(response , url):
    call = requests.get(url)
    status = call.status_code
    next_url = call.json()["next"]
    response.append(call.json()["results"])

    return response, next_url, status

def api_call():
    response = []
    response, next_url, status = api_request(response, "https://swapi.dev/api/starships")

    while next_url is not None:
        place_holder1, next_url, status = api_request(response , next_url)
    return response






