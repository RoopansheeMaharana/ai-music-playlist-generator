import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "b96e07ca10a64e8aa6e8d39c0e5d3088"
client_secret = "430ada2fc1ed48d080a2852bd1561d08"

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search(q="Shape of You", type="track", limit=1)

print(results)