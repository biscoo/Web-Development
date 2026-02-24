import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
Empire_page = response.text
soup = BeautifulSoup(Empire_page, "html.parser")

movies = soup.find_all(name="h3", class_="title")

ml = []
for m in movies:
    ml.append(m.getText())
ml_rev = ml[::-1]
with open("movies.txt", "w", encoding="utf-8") as file:
    for m in ml_rev:
        file.write(m+'\n')

