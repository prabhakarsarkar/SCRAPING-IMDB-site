# import requests,json,os
# from bs4 import BeautifulSoup
# from link import url2
# from pprint import pprint

# def movie_type(link):
# 	a=0
# 	if os.path.exists("gener.json"):
# 		with open("gener.json","r") as file:
# 			data=json.load(file)
# 			print("yes")
# 			return data
# 	else:
# 		print("else")
# 		gener=[]
# 		for i in (link):
# 			res=requests.get(i)
# 			soup=BeautifulSoup(res.text,"html.parser")
# 			gener1=soup.find("div",class_="subtext").a.text.strip()
# 			gener.append(gener1)
# 			a+=1
# 			with open("gener.json","w+") as file:
# 				data=json.dump(gener,file)
# 				print("no"," ",a)
# 		return gener

# gener=movie_type(url2)
# def movie_gener(gener):
# 	lis=[]
# 	for i in gener:
# 		if i not in lis:
# 			lis.append(i)
# 	dic={}
# 	for j in lis:
# 		# print(j)
# 		a=0
# 		for n in gener:
# 			if j==n:
# 				a+=1
# 			dic[j]=a
# 	pprint(dic)
# movie_gener(gener)
