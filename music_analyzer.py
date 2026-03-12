import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_id = "b96e07ca10a64e8aa6e8d39c0e5d3088"
client_secret = "430ada2fc1ed48d080a2852bd1561d08"

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Search for songs
results = sp.search(q="year:2024", type="track", limit=10)
songs_data = []

for item in results['tracks']['items']:
    song_name = item['name']
    artist = item['artists'][0]['name']
    album = item['album']['name']
    duration = item['duration_ms']

    songs_data.append({
        "Song": song_name,
        "Artist": artist,
        "Album": album,
        "Duration_ms": duration
    })

df = pd.DataFrame(songs_data)

df.to_csv("spotify_songs_dataset.csv", index=False)

print("Dataset created successfully!")
print(df)