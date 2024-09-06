import os
import json
import requests
from datetime import datetime

# Input url and request keys, matching the dict key to the
# api url segment
url = "https://api.nasa.gov/planetary/apod?"

keys = dict(
    api_key = "ROZpi2Du6BFMDqh2EEW9RZmzEjQ09Rk4qk7mbulk",
)

os.chdir("./data")
date = datetime.today().strftime('%Y-%m-%d')
# Only make an API call if the data hasn't already been collected
if not os.path.isfile(date+".json"):
    # Initial call, returns a Response object from the given url.
    # If keys are provided, builds them into the url
    call = requests.get(url,keys)
    # Returns the API response's headers as a dict
    # The headers property of a request is a dict by default
    headers = call.headers
    # Converts the JSON response into a dict
    # Takes the text of the response and turns it into a dict
    response = json.loads(call.text)
    allowance = {"Remaining Calls":headers._store['x-ratelimit-remaining'][1]}
    response.update(allowance)
    # Writes the json response to a file named using the date
    # of the response
    with open(date+".json",'w') as pad:
        pad.write(json.dumps(response))
else:
    with open(date+".json",'r') as data:
        response = json.loads(data.read())
os.chdir("../photo data")
# Only check for/download the image if it hasn't been downloaded
if not os.path.isfile(response["title"]+".jpg"):
    # Uses the response's image URL to save the photo from the
    # byte formatted answer
    photo = requests.get(response["url"]).content

    with open(response["title"]+".jpg",'wb') as canvas:
        canvas.write(photo)