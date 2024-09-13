# What is This?
Ideally, it will become a basic website that will allow a user to view, download, and bookmark entries in a database built up of data collected from NASA's Astronomy Photo of the Day API.

Astropic is a project I came up with mainly as a way to learn python, some networking, and web server hosting. I mostly want to keep a repo just to keep track of this learning. Honestly sorta hoping I'm the only one to see this, but feel free to check it out if you're here! :)
# Implemented
- API call only if one has not been made that day
- When making an API call, saves the response as a .json
- If a call has been made that day (Checks for a file named YYYY-MM-DD) use that instead
# To Do
## App
[ ] Add attribute to track favorites
[ ] Start keeping the .jsons as a database
## Site
[ ] Set up Pi on local network as a server that can have an html file updated on command
[ ] Page to display today's photo
[ ] Option to download the day
[ ] Option to bookmark the day
[ ] Gallery of the last week (month?)
[ ] Favorites menu