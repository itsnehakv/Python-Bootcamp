from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ["SPOTIFY_DISPLAY_NAME"],
    )
)
user_id = sp.current_user()["id"]

# date=input("Which year would you like to travel to? (YYYY-MM-DD format please!)\n")
date="2005-11-17"
BILLBOARD_URL=f"https://www.billboard.com/charts/hot-100/{date}"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

'''https://www.whatismybrowser.com/detect/what-is-my-user-agent/'''

billboard_response=requests.get(url=BILLBOARD_URL, headers=header)
billboard_txt=billboard_response.text

soup=BeautifulSoup(billboard_txt, "html.parser")

song_titles=[title.getText().strip() for title in soup.select("li ul li h3")]

print(song_titles)

song_artists=[artist.getText() for artist in soup.select("li ul li span a")]
print(song_artists)

