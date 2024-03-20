import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import base64
import re
import time

# Spotify API credentials
SPOTIFY_CLIENT_ID = '40d5bc53188f4040a49254f469b7abad'
SPOTIFY_CLIENT_SECRET = '3998aa6f24294e019611129596a60ddb'

# Selenium with Firefox WebDriver
def download_song(url):
    driver = webdriver.Firefox()
    driver.get('https://your_download_website.com')  # Replace with the actual download website URL

    # Assuming there is an input box with the id 'urlInput' and a download button with the id 'downloadButton'
    url_input = driver.find_element_by_id('urlInput')
    download_button = driver.find_element_by_id('downloadButton')

    # Input the URL and click the download button
    url_input.send_keys(url)
    download_button.click()

    # Wait for some time to ensure the download is complete (adjust as needed)
    time.sleep(10)

    # Move the downloaded file to the specified directory
    downloaded_file_path = 'path/to/downloaded/files'  # Update with the actual download directory
    output_directory = 'path/to/save/songs'  # Update with the actual save directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(downloaded_file_path):
        file_path = os.path.join(downloaded_file_path, file_name)
        if os.path.isfile(file_path):
            os.rename(file_path, os.path.join(output_directory, file_name))

    driver.quit()

# Get Spotify playlist tracks
def get_spotify_playlist_tracks():
    playlist_id = 'https://open.spotify.com/album/2Zzk6zrMzW0V5lPXdM1eRR'  # Replace with the actual playlist ID

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'.encode()).decode()
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    song_data = []

    for track in data['items']:
        # Assuming the Spotify playlist contains YouTube URLs in the 'external_urls' field
        youtube_url = track['track']['external_urls']['youtube']
        song_data.append(youtube_url)

    return song_data

if __name__ == "__main__":
    song_urls = get_spotify_playlist_tracks()

    for url in song_urls:
        # Download song using Selenium
        download_song(url)

    print("Download complete.")
