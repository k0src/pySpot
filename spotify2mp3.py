import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search
import tkinter as tk
from tkinter import filedialog
import os
import keys

client_id = keys.client_id
client_secret = keys.client_secret
# 111
# Test comment
# heeel

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_info(link):
    track_id = link.split('/')[-1].split('?')[0]

    try:
        track_info = sp.track(track_id)

        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']

        return track_name, artist_name
    except Exception as e:
        print('Error:', e)
        return None, None
    
def youtube_search(search_term):
    query = Search(search_term)
    if query:
        return f'https://www.youtube.com/watch?v={query.results[0].video_id}'
    
    return None

def download_mp3(ytlink):
    directory_path = filedialog.askdirectory()

    yt = YouTube(ytlink)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=directory_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)




link = input('Enter Spotify link: ')

track_name, artist_name = get_track_info(link)
search_term = f'{track_name} - {artist_name}'
ytlink = youtube_search(search_term)

print(search_term)
print(youtube_search(search_term))

download_mp3(ytlink)
