from pprint import pprint
from task13 import data
actors1 = {}
for cast in data:
	count = 0
	for actors in cast[0:5]:
		count+=1 
		if count==1:
			main_actor_id = actors["imdb_id"]
			if main_actor_id not in actors1:
				actors1[main_actor_id]={}
				actors1[main_actor_id]["name"]=actors["name"]
				actors1[main_actor_id]["frequent_co_actors"]=[]
		else:
			flag = True
			for j in actors1[main_actor_id]["frequent_co_actors"]:
				if j['imdb_id']==actors["imdb_id"]:
					flag = False
					break
			if flag:
				actors["num_of_movie"]=1
				actors1[main_actor_id]["frequent_co_actors"].append(actors)
			else:
				for j in actors1[main_actor_id]["frequent_co_actors"]:
					if j["imdb_id"]==actors["imdb_id"]:
						j["num_of_movie"]+=1

pprint(actors1)