import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
import os
import keys

client_id = keys.client_id
client_secret = keys.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def download_mp3(spotlink):
    directory_path = filedialog.askdirectory()

    track_id = spotlink.split('/')[-1].split('?')[0]
    track_info = sp.track(track_id)

    track_name = track_info['name']
    artist_name = track_info['artists'][0]['name']

    search_term = f'{track_name} - {artist_name}'

    query = Search(search_term)
    ytlink = f'https://www.youtube.com/watch?v={query.results[0].video_id}'

    yt = YouTube(ytlink)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=directory_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

window = ttk.Window(themename="darkly")
window.title("pySpot")
window.geometry('500x500')
window.maxsize(500, 500)
window.minsize(500, 500)

link_var = tk.StringVar()

title = ttk.Label(window, text="pySpot", font = 'Calibri 24 bold', foreground='lightblue')
title.pack(pady=5)

link_label = ttk.Label(window, text="Enter Spotify Link", font = 'Calibri 12')
link_label.pack(pady=5)

link_entry = ttk.Entry(window, width=50, textvariable=link_var)
link_entry.pack(pady=5)

download_button = ttk.Button(window, text="Download", command=lambda: download_mp3(link_var.get()))
download_button.pack(pady=5)

window.mainloop()