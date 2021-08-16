
# Instructions
The character data in your MongoDB database has been pulled from https://swapi.dev/. As well as 'people',
the API has data on starships. Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship. Use these to replace 'pilots' with a
list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

You have until 11am on Monday.

INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable

# Pseudocode
## Accessing the Starships and Characters APIs
### Check that you can access the APIs and the length of returned list is as expected
* Use import requests, set url variables to the url of the apis, set request variables to results.get(url),
then finally use a data variable to set the request variables .json() so that the data is returned to the programme
in json format.

* Use loop based on the number of pages to specify the url. Add all entries to a list or dict that is set to individual
variables, so that they can be called.

## Create list of pilots for each starship from Starships
### Check that the first name of the first pilot is the same in the list as expected
* Create a for loop to place the list of pilots from each starship into a separate list

* Remove any lists that are empty, then for each entry, find the names of all the pilots, and store them within
another list. 

## Use the names stored in the list to find their ObjectID
### Check that the number of stored object ids are equal to the number of names 
Iterate over the list of lists, find and store the ObjectId for each name that matches the character from our 
characters' dataset. 

## Add the starship database to the local mongodb starwars database
### Check that the number of inserted documents is as expected
Use pymongo to add the dataset to mongodb


## Replace the pilots ids with the ids of the characters from the local characters database
### Check that the first pilot objectId matches that from the previously created list of object ids
Use pymongo to update the entries that have pilots, and replace the links with the character's respective object id,
that refers to their character document within the local character database