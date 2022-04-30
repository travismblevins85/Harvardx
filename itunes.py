import sys
import json
import requests
# type python itunes.py in cmd prompt with band name, "weezer" in this instance
# brings back json data in a dictionary format
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2)) Prints the json out prettier than just regular print
# Now trying to find "trackName" inside of 2 dictionaries and a list of json data
o = response.json()
for result in o["results"]:
    print(result['trackName'])