import requests,pprint,os,json
from bs4 import BeautifulSoup

def url():
	if os.path.exists("jsonfile.json"):
		with open("jsonfile111.json","r") as file:
			# print("yes")
			data=json.load(file)
			return data
	else:
		resp=requests.get(" https://www.imdb.com/india/top-rated-indian-movies/")
		soup=BeautifulSoup(resp.text,"html.parser")
		url=soup.find("tbody",class_="lister-list")
		trs=url.find_all("tr")
		lin=[]
		for i in trs:
			ul=i.find("td",class_='titleColumn').a["href"]
			li="https://www.imdb.com/"+ul
			lin.append(li)
		with open("jsonfile.json","w+") as file:
			# print("no")
			data = json.dump(lin,file)
			return lin
url2=url()
# print(url2)