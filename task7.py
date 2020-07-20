########################## task 7 ################################:
import requests,json
from pprint import pprint
from bs4 import BeautifulSoup
from task5 import get_movie_list_details
from task1 import scrape_top_list
def analyse_movies_directors(movie_dirceter):
	dirceters={}
	for dirceter in movie_dirceter:
		a=""
		for i in dirceter["director"]:
			a+=i
		if a not in dirceters:
			dirceters[a]=1
		else:
			dirceters[a]+=1
	return dirceters

dirceter_analyse=analyse_movies_directors(get_movie_list_details(scrape_top_list()[0:5]))
pprint(dirceter_analyse)