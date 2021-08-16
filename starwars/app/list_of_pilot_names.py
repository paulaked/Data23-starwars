from starwars.app.starships_api_request import starships_api_request
import requests


def list_of_pilot_names():
    starships = starships_api_request()

    pilots = []
    pilot_names = []

    for starship in starships:
        pilots.append(starship["pilots"])

    for pilot_list in pilots:
        if not pilot_list:
            continue
        else:
            new_pilot_list = []
            for pilot in pilot_list:
                character_request = requests.get(pilot)
                character_data = character_request.json()
                character_name = character_data["name"]
                new_pilot_list.append(str(character_name))
            pilot_names.append(new_pilot_list)
    return pilot_names
