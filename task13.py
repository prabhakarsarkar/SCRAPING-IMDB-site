# from task4 import detle
# from pprint import pprint
# from link import url2
# import requests,json,os
# from bs4 import BeautifulSoup
# def l(i,n):
# 	lis=[]
# 	if os.path.exists("all_movie_detailes.json"):
# 		with open("all_movie_detailes.json","r") as file:
# 			data=json.load(file)
# 			return data

# 	else:
# 		for j in range(len(i)):
# 			s=i[j][28:37]
# 			url=s
# 			file1=s+".json"
# 			res=requests.get("https://www.imdb.com/title/"+url+"/fullcredits?ref_=tt_cl_sm#cast")
# 			soup=BeautifulSoup(res.text,"html.parser")
# 			actor=soup.find("table",class_="cast_list")
# 			td=actor.find_all("td",class_="")
# 			lis1=[]
# 			for t in td:
# 				dic={}
# 				q=t.find("a").get("href")
# 				id_imdb=q[6:15]
# 				name=t.find("a").text.strip()
# 				dic["imdb_id"]=id_imdb
# 				dic["name"]=name
# 				lis1.append(dic)
# 			lis.append(lis1)
# 			n[j]["Cast"]=lis1
# 		with open("all_movie_detailes.json","w+") as file:	
# 			data = json.dump(lis,file)
# 		return lis
# data = l(url[0,20],detle)
# # pprint(data)

for i in range(10,100):
	for j in range(10,100):
		k=(i*j)

		b=k[::-1]