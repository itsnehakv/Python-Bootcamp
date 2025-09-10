import requests
from bs4 import BeautifulSoup

movie_response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_response_text=movie_response.text

soup=BeautifulSoup(movie_response_text, "html.parser")

movie_titles=[title.getText() for title in soup.find_all(name="h3", class_="title")]
print(movie_titles)

movie_titles.reverse()
print(movie_titles)

with open("movies.txt","w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

'''encoding="utf-8", which supports all characters
or else error from "fancy" chars like è,ê, ë,ē, ė,ę'''