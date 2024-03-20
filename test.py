import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import base64
import re
import time

def get_spotify_playlist_tracks():
    playlist_id = '2Zzk6zrMzW0V5lPXdM1eRR'  # Replace with the actual playlist ID

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{"40d5bc53188f4040a49254f469b7abad"}:{"3998aa6f24294e019611129596a60ddb"}'.encode()).decode()
    }

    print("Making API request...")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        print("API request successful.")

        # Print the response content for debugging
        print(response.text)

        data = response.json()

        # Print the structure of the 'data' dictionary
        print(data)

        song_data = []

        for track in data.get('items', []):
            # Assuming the Spotify playlist contains YouTube URLs in the 'external_urls' field
            youtube_url = track['track']['external_urls']['youtube']
            song_data.append(youtube_url)

        return song_data
    else:
        print("API request failed.")

get_spotify_playlist_tracks()