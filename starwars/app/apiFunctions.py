import requests


# Extracts all the results documents from the starting link
# Enters next link and repeats
# Until next link is NULL
# Results are stored in a list
def extract_until_null(starting_url: str, storage: list):
    link = requests.get(starting_url)
    next_link = link.json()['next']
    while next_link is not None:
        extract_from_page(link, storage)
        link = requests.get(next_link)
        next_link = link.json()['next']
    extract_from_page(link, storage)

# For every result in the link it adds it to a list]#
# This function is called in the extract_until_nul function
def extract_from_page(response : requests.models.Response, storage:list):
    for i in range(len(response.json()['results'])):
        storage.append(response.json()['results'][i])



