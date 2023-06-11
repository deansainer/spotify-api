from django.http import HttpResponse
from django.shortcuts import render
import spotipy
import re
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import *
CLIENT_ID = "f155cfe6384f4fd0b45c91a57c5c2233"
CLIENT_SECRET = "515b30aee41241b7a37f790f5c03ce5e"

# authenticate
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# create spotify session object
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get list of tracks in a given playlist


class Track:
    def __init__(self, name, artist, link, image, preview):
        self.track_name = name
        self.artist_name = artist
        self.link = link
        self.image = image
        self.preview = preview


def index(request):
    uri = request.GET.get('uri', 'https://open.spotify.com/playlist/35Ux8wZHG7balGjo2Zc2Uz?si=96bd3a09905f4dc0')
    uri = re.findall(r"\/playlist\/(\w+)", uri)
    uri = uri[0]
    items = session.playlist_tracks(uri)["items"]
    form = UriForm()

    track_list = []

    for item in items:
        track_name = item["track"]["name"]
        artist_name = item["track"]["artists"][0]["name"]
        link = item["track"]["external_urls"]["spotify"]
        image = item["track"]["album"]["images"][0]["url"]
        preview = item["track"]["preview_url"]
        track = Track(track_name, artist_name, link, image, preview)
        track_list.append(track)
    context = {'track_list': track_list, 'form': form}
    return render(request, 'spotify_app/index.html', context)