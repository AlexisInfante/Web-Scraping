from requests import get
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top?sort=rk,asc&mode=simple&page=1"

html_file = get(url)
html_soup = BeautifulSoup(html_file.text, "html.parser")

movie_ranking = []
movie_name = []
movie_year = []
movie_score = []

movie_container = html_soup.find('tbody', class_ = 'lister-list')
individual_containers = movie_container.find_all('tr')

for movie in individual_containers:

	movie_ranking.append(int(movie.find('td', class_ = 'posterColumn').span.get('data-value')))
	movie_name.append(movie.find('td', class_ = 'titleColumn').a.text)
	movie_year.append(movie.find('td', class_ = 'titleColumn').span.text.translate({ord(i): None for i in '()'}))
	movie_score.append(float(movie.find('td', class_ = 'ratingColumn imdbRating').strong.text))


with open('IMDb_250.csv', 'w', newline = '') as f:
	writer = csv.writer(f)
	writer.writerow(['Ranking', 'Name', 'Year', 'IMDb Score'])
	for i in range(0,len(movie_ranking)):
		writer.writerow([movie_ranking[i], movie_name[i], movie_year[i], movie_score[i]])

f.close()


