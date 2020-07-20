import requests,json,os
from bs4 import BeautifulSoup
from pprint import pprint
from link import url2

def all_detels(i):
	for j in i:
		s=j[28:37]
		url=s
		file1=s+".json"
		if os.path.exists("task12.json"):
			with open("task12.json","r") as file:
				data = json.load(file)
			return data
		else:
			print("else")
			res=requests.get("https://www.imdb.com/title/"+url+"/fullcredits?ref_=tt_cl_sm#cast")
			# print(url)
			soup=BeautifulSoup(res.text,"html.parser")
			actor=soup.find("table",class_="cast_list")
			td=actor.find_all("td",class_="")
			lis=[]
			for i in td:
				dic={}
				n=i.find("a").get("href")
				id_imdb=n[6:15]
				name=i.find("a").text.strip()
				dic["imdb_id"]=id_imdb
				dic["name"]=name
				lis.append(dic)
			
			
				with open("task12.json","w+") as file:
					data = json.dump(lis,file)
					print("coming")
				# return data
data1=all_detels(url2)
# print(data1)


