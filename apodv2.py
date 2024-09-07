# Enables file system interaction
import os
# Allows json manipulation
import json
# Enables API requests
import requests
# For checking file existance by name
from datetime import datetime

# Input url and request keys, matching the dict key to the
# api url segment
url = "https://api.nasa.gov/planetary/apod?"

location = os.getcwd()

keys = dict(
    api_key = "",
)

# change to data folder, if its not there, make it
try:
    os.chdir(location+"/data")
except:
    os.mkdir(location+"/data")
    os.chdir(location+"/data")

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

# change to photo data folder, if its not there, make it
try:
    os.chdir("./photos")
except:
    os.mkdir("./photos")
    os.chdir("./photos")

# Only check for/download the image if it hasn't been downloaded
if not os.path.isfile(response["title"]+".jpg"):
    
    # Uses the response's image URL to save the photo from the
    # byte formatted answer
    photo = requests.get(response["url"]).content
    with open(response["title"]+".jpg",'wb') as canvas:
        canvas.write(photo)
