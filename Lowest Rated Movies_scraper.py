from requests import get
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/bottom?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=B7869BCS5DRP7CV1NP6K&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_8"

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


with open('Lowest Rated Movies.csv', 'w', newline = '') as f:
	writer = csv.writer(f)
	writer.writerow(['Ranking', 'Name', 'Year', 'IMDb Score'])
	for i in range(0,len(movie_ranking)):
		writer.writerow([movie_ranking[i], movie_name[i], movie_year[i], movie_score[i]])

f.close()


