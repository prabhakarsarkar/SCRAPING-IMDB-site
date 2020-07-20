import requests,pprint,os,json,random,time
from bs4 import BeautifulSoup
from link import url2	
def fun(u):
	random_time=random.randint(1,3)
	# print("no")
	list1=[]
	a=0
	for k in u:
		movie_id=""
		for j in k[28:]:
			if j=="/":
				break
			else:
				movie_id+=j
			file=movie_id+".json"
		if os.path.exists("jsonFiles/"+file):
			with open("jsonFiles/"+file,"r") as file1:
				data1=json.load(file1)
				return data1
		else:
			time.sleep(random_time)
			print("yes")
			res=requests.get(k)
			soup=BeautifulSoup(res.text,"html.parser")
			name=soup.find("div",class_="title_wrapper").h1.text
			movie_name=""
			for j in name:
				if j!= "(":
					movie_name=(movie_name+j)
				else:
					break
			################# find movie runtime code #############################

			time1=soup.find("div",class_="subtext").time.text.strip()
			hours=int(time1[0])*60
			movie_runtime=0
			if "min" in time1:
				minutes=int(time1[3:].strip("min"))
				movie_runtime=minutes+hours
			else:
				movie_runtime=hours
			# print(movie_runtime)
		# 	###################### find movie genre  code ######################
			gener=[]
			gener1=soup.find("div",class_="subtext").a.text.strip()
			gener.append(gener1)

		# 	############################finddriector name code ########################
			director=soup.find("div",class_="credit_summary_item").a.text

		# 	######################## find movte poster code #########
			link=soup.find("div",class_="poster").a["href"]
			poster_link="https://www.imdb.com/"+link
		# 	################# find movie bio code ######################
			movie_bio=soup.find("div",class_="summary_text").text.strip()
			# print(movie_bio)
		# 	########################### find country amd language code ################
			
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
			list1.append(dic)
			a+=1
		with open("jsonFiles/"+file,"w+") as file1:
				data1=json.dump(list1,file1)
				print("ban gayi"," ",a)
		return data1


data=fun(url2)
# print(data)

