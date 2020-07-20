from pprint import pprint
from task1 import scrape_top_list
def group_by_year(movie):
	lis={}
	for j in movie:
		list1=[]
		for n in movie:
			if j["year"]==n["year"]:
				list1.append(n)
		lis[j["year"]]=list1
	return lis
			
byYear=group_by_year(scrape_top_list())
pprint(byYear)
