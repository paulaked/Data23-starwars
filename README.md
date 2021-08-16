# Data 23 Star Wars Project

## Functionality
This package updates a mongodb database called, starwars with a collection called starship. It extracts the data from the swapi api and updates it so that the pilot category has an object id pointing to the related object in the character collection on the mongo db database.

## How to use
Currently this package does not take any user inputs. It does however allow for for changes in the swapi database. As long as the general results schema stays the same it will work even if multiple new entries are added, removed or values changed.

## Further work
Currently the code requires a lot of api calls and uses two different function to call the api for starships and characters. A significant cause of this is that an api call is made for each pilot, and every occurrence of that pilot. It may be quicker to call all of the pilot data at once and it would be quicker to only make one call per pilot.

Another option would be to call the characters data and replace the current character category with this data, this would allow for a shorter package run time, as it would only require one api call per page of data and shorter processing time as the object ids could be added straight from Mongodb by querying the URL tag.

I would also like to update the package to call all the data from swapi and add it to the database and then replace all URL’s with object ids.


## Trello Board Link
https://trello.com/b/rBvZSFFh/starwars
