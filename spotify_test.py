import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search(q="Shape of You", type="track", limit=1)


print(results)
