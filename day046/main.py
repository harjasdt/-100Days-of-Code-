#used python spotify api(spotipy to make a playlist of top 100 songs of the given date
import datetime as dt
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="your id",
        client_secret="your secret",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# input=input("ENTER DATE")
input="2000/8/12"
format = '%Y/%m/%d'

# convert from string format to datetime format
datetime = dt.datetime.strptime(input, format)
d=datetime.date()
response=requests.get(f"https://www.billboard.com/charts/hot-100/{d}").text
d=str(datetime.date())
soup=BeautifulSoup(response,"html.parser")
titles = soup.select(selector="div li ul li h3")
title_list = [i.getText().strip() for i in titles]
# print(title_list)
song_uris = []
year = d.split("-")[0]
for song in title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
