from task4 import scrape_movie_details
from bs4 import BeautifulSoup
from task1 import scrape_top_list
from pprint import pprint


def get_movie_list_details(movies):
	movie_details = []
	for movie in movies:
		url = movie["url"]
		data = scrape_movie_details(url)
		movie_details.append(data)
	return movie_details

# data = get_movie_list_details(scrape_top_list()[0:5])
# pprint(data)