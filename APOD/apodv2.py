# Enables file system interaction
import os.path
# Allows json manipulation
import json
# Enables API requests
import requests
# For checking file existance by name
from datetime import datetime
# date for checking file existance/naming
date = datetime.today().strftime('%Y-%m-%d')
# change to data folder, if its not there, make it
try:
    os.chdir("APOD/data")
except:
    os.mkdir("APOD/data")
    os.chdir("APOD/data")
    print("data folder created...")
# Only make an API call if the data hasn't already been collected
if not os.path.isfile(date+".json"):
    # Input url and 
    url = "https://api.nasa.gov/planetary/apod?"
    # Reads the API key from a text file named api_key.txt in 
    # a folder named secrets for the api key
    with open("../secrets/api_key.txt",'rt') as key:
        """
        input the desired request keys, matching the dict key to the
        api url segment
        """
        keys = dict(
            api_key = key.read(),
        )
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
    response["title"] = response["title"].replace(':','')
    response["title"] = response["title"].replace(' ','-')
    # Writes the json response to a file named using the date
    # of the response
    with open(date+".json",'w') as pad:
        pad.write(json.dumps(response))
else:
    with open(date+".json",'r') as data:
        response = json.loads(data.read())
    print("Aleady have today's JSON!")
# change to photo subfolder, if its not there, make it
try:
    os.chdir("./photos")
except:
    os.mkdir("./photos")
    os.chdir("./photos")
    print("photos folder created...")
# Windows >:(
filename = response["title"]
# Only check for/download the image if it hasn't been downloaded
if not os.path.isfile(filename+".jpg"):
    
    # Uses the response's image URL to save the photo from the
    # byte formatted answer
    photo = requests.get(response["hdurl"]).content
    with open(filename+".jpg",'wb') as canvas:
        canvas.write(photo)
    print(date+"'s photo saved!")
else:
    print(date+"'s photo is already saved!")