def randomApods(num):
    import requests
    keys = dict(
        api_key = "ROZpi2Du6BFMDqh2EEW9RZmzEjQ09Rk4qk7mbulk",
        endpoint = "https://api.nasa.gov/planetary/apod?",
        count = str(num),
    )
    response = requests.get(keys["endpoint"] + "api_key=" + keys["api_key"] + "&count=" + keys["count"])

    # Dictionary made of the response attributes
    pics = response.json()
    for pic in pics:
        img = requests.get(pic["url"])
        name = pic["title"]
        with open(name+".jpg", 'wb') as handler:
            handler.write(img.content)
        return response.text
def apod():
    import requests
    # Temporary, endpoint and keys will be parameters of the function eventually
    endpoint = "https://api.nasa.gov/planetary/apod?"
    keys = dict(
        api_key = "ROZpi2Du6BFMDqh2EEW9RZmzEjQ09Rk4qk7mbulk",
    )
    # Sets request to just the endpoint url, this avoids starting the url with endpoint=.
    # ^ I know I can do that a better way.
    request = endpoint
    # iterates through provided keys and adds the dict item name to the url with its
    # corresponding value. Keys must be ordered as the endpoint expects in the provided dict
    for key in keys:
        request += key + "=" + keys[key]
    response = requests.get(request)
    # uses the response's url to download the daily image, pulled from a dict created from the response
    pic = response.json()
    img = requests.get(pic["url"])
    name = pic["date"] + " " + pic["title"]
    # writes the image to a .jpg file, then the full json string to a .txt file
    with open(name+".jpg",'wb') as handler:
        handler.write(img.content)
    with open(name+".txt","w") as pad:
        pad.write(response.text)
    # returns the response json
    return response.text

# trying to get the date, then check for a file that starts with it
# if it's there, then do the api call. Otherwise, just use the files
# already downloaded. Can't waste my api calls :)
# Times needed new key: 1

import json
import requests

url = "https://api.nasa.gov/planetary/apod?"

keys = dict(
    api_key = "ROZpi2Du6BFMDqh2EEW9RZmzEjQ09Rk4qk7mbulk",
)

ans = requests.get(url,keys)
ans = ans.json()
img = requests.get(ans["url"])
    
name = ans["date"] + " " + ans["title"]
with open(name+".jpg",'wb') as canvas:
    canvas.write(img.content)
with open(name+".json","w") as pad:
    pad.write(json.dumps(ans))
