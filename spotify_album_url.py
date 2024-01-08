import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify credentials
client_id = ''
client_secret = ''

# Setting up Spotify client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_album_image_url(track_name):
    # Search for the track
    result = sp.search(q='track:' + track_name, type='track', limit=1)
    items = result['tracks']['items']
    if items:
        # Get album image URL
        album_image_url = items[0]['album']['images'][0]['url']
        return album_image_url
    else:
        return "Not Found"

# Read the dataset
df = pd.read_csv('C:/Users/ayush/Desktop/Excel Datasets/spotify-2023.csv')

# Assuming the column name for track names is 'track_name'
df['album_image_url'] = df['track_name'].apply(get_album_image_url)

# Save the new dataframe with album image URLs
df.to_csv('C:/Users/ayush/Desktop/Excel Datasets/spotify-2023.csv', index=False)
