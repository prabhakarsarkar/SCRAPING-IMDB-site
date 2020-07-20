import requests,json,os
from pprint import pprint
from bs4 import BeautifulSoup
lis=[]
def scrape_top_list():
	# here i am chacking data if already exists or not
	if os.path.exists("jsonFiles/task1.json"):
		with open("jsonFiles/task1.json","r") as file:
			data = json.load(file)
			return data
	else:
		# here i am putting requests
		url=" https://www.imdb.com/india/top-rated-indian-movies/"
		res=requests.get(url)
		soup=BeautifulSoup(res.text,"html.parser")
		main_div=soup.find("div",class_="lister")
		tbody=main_div.find("tbody",class_="lister-list")
		trs=tbody.find_all("tr")

		name=[]
		year=[]
		position=[] 
		rating=[]
		url=[]
		a=0
		for tr in trs:
			posi=tr.find("td",class_="titleColumn")
			a+=1
			position.append(a)
			yer=tr.find("td",class_="titleColumn").span.get_text()
			year.append(yer)
			nam=tr.find("td",class_="titleColumn").a.text
			name.append(nam)
			rat=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
			rating.append(rat)
			ul=tr.find("td",class_="titleColumn").a["href"]
			link="https://www.imdb.com/"+ul
			url.append(link)
		for i in range(len(position)):
			dic={}
			dic["name"]=str(name[i])
			year[i]=year[i][1:5]
			dic["year"]=int(year[i])
			dic["position"]=(position[i])
			dic["url"]=(url[i])
			lis.append(dic)
			pprint(lis)
	with open("jsonFiles/task1.json","w") as file:
		json.dump(lis,file)
		return(lis)

# top_movie=scrape_top_list()