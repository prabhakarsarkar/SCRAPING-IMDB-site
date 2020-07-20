import requests,json
from bs4 import BeautifulSoup
from pprint import pprint
from task1 import scrape_top_list
def scrape_movie_details(url):

	res=requests.get(url)
	soup=BeautifulSoup(res.text,"html.parser")

	# find movie name code 
	name=soup.find("div",class_="title_wrapper").h1.text
	movie_name=""
	for j in name:
		if j!= "(":
			movie_name=(movie_name+j)
		else:
			break
	# find movie runtime code 

	time1=soup.find("div",class_="subtext").time.text.strip()
	hours=int(time1[0])*60
	movie_runtime=0
	if "min" in time1:
		minutes=int(time1[3:].strip("min"))
		movie_runtime=minutes+hours
	else:
		movie_runtime=hours
	# find movie genre  code
	gener=[]
	gener1=soup.find("div",class_="subtext").a.text.strip()
	gener.append(gener1)

	# find driector name code 
	director=soup.find("div",class_="credit_summary_item").a.text

	# find movte poster code 
	link=soup.find("div",class_="poster").a["href"]
	poster_link="https://www.imdb.com/"+link
	# find movie bio code
	movie_bio=soup.find("div",class_="summary_text").text.strip()
	# print(movie_bio)
	# find country amd language code 
	
	div=soup.find('div',class_='article',id='titleDetails')
	div1=div.find_all("div",class_="txt-block")
	for i in div1:
		try:
			if i.h4.text == "Country:":
				country = (i.a.text)
				# print (country)
			elif i.h4.text =="Language:":
				language_a = i.find_all('a')
				language_lis=[]
				for j in language_a:
					language = ""
					language += j.text
					language_lis.append(language)
				# print(language_lis)
		except AttributeError:
			continue
	dic={}
	dic["movie_name"]=movie_name
	dic["director"]=director
	dic["country"]=country
	dic["language"]=language_lis
	dic["poster_url"]=poster_link
	dic["bio"]=movie_bio
	dic["rumtime"]=movie_runtime
	dic["gener"]=gener
	return dic

movieData=scrape_movie_details(scrape_top_list()[0]["url"])
# pprint(movieData)