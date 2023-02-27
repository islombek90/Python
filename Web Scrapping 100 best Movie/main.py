import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇



response = requests.get(URL)
web_scrap = response.text

soup = BeautifulSoup(web_scrap, "html.parser")

titles = soup.findAll("h3")

movie_list = [movies.getText() for movies in titles]
print(movie_list)

movies = movie_list[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(movie)

