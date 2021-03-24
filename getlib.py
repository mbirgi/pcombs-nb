import spotify
import utils

sp = spotify.login(scope='playlist-modify-private playlist-read-private')
user = sp.current_user()
username = user['id']
displayName = user['display_name']
print("Logged in user: " + displayName + "(" + username +")")

# get all my playlists 
response = sp.current_user_playlists()
all_playlists = response['items']
while response['next']:
    response = sp.next(response)
    all_playlists.extend(response['items'])
playlists = [{'id': pl['id'], 'name': pl['name'], 'desc': pl['description'], 'tracks': pl['tracks']['total']} for pl in all_playlists]
print("Number of playlists retrieved: " + str(len(playlists)))

# 