import requests,pprint,os,json
from bs4 import BeautifulSoup
from task5 import get_movie_list_details
from task1 import scrape_top_list
from pprint import pprint

def analyse_movies_language(movie_list):
	languages = {}
	for movie in movie_list:
		for lang in movie["language"]:
			print(lang)
	# 		if lang not in languages:
	# 			languages[lang]=1
	# 		else:
	# 			languages[lang]+=1
	# return languages

language_analysis = analyse_movies_language(get_movie_list_details(scrape_top_list()[0:5]))
# pprint(language_analysis)


