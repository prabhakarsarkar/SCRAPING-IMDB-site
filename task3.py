from task1 import scrape_top_list
from pprint import pprint
def group_by_decade(movies):
	years = {}
	for i in movies:
		year = i["year"]
		year = str(year)
		decade = year[0:3]
		decade+="0"
		decade = int(decade)
		if decade not in years:
			years[decade]=[]
			years[decade].append(i)
		# else:
		# 	years[decade].append(i)
	return years

byDecade=group_by_decade(scrape_top_list())
pprint(byDecade)
