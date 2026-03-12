import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("spotify_songs_dataset.csv")

# Use duration as feature
features = df[["Duration_ms"]]

# Calculate similarity
similarity = cosine_similarity(features)

# Choose a song
song_name = input("Enter a song name: ")

# Find song index
song_index = df[df["Song"].str.lower() == song_name.lower()].index

if len(song_index) == 0:
    print("Song not found in dataset.")
else:
    song_index = song_index[0]

    scores = list(enumerate(similarity[song_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Playlist:\n")

    for i in scores[1:6]:
        print(df.iloc[i[0]]["Song"], "-", df.iloc[i[0]]["Artist"])