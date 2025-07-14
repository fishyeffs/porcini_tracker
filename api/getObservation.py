import requests, math

def getObservation():
	per_page = 200
	page=1
	params = {
		"taxon_id" : 48701,
		"iconic_taxa" : "Fungi",
		"per_page" : per_page,
		"place_id" : 6857
	}

	#to ensure we don't suckerpunch the api
	desiredResult=1000
	response = requests.get("https://inaturalist.org/observations.json", params)
	mushroomList = response.json()
	returnedResults=int(response.headers.get("X-Total-Entries",0))
	#print(f"Number of results:  {returnedResults}")
	## return pages per 1000, or if returnedResults is less than 1000, do not exceed returned pages
	if (returnedResults > desiredResult):
		pages = math.floor(desiredResult / per_page) 
	else:
		pages = math.floor(returnedResults / per_page)
	#print("HTTP Response: ", response.json())
	
	while(page<pages):
		page+=1
		params = {
			"taxon_id" : 48701,
			"iconic_taxa" : "Fungi",
			"per_page" : per_page,
			"page" : page,
			"place_id" : 6857
		}
		response = requests.get("https://inaturalist.org/observations.json", params)
		mushroomList += response.json()
	
	for i in mushroomList:
		i["latitude"] = float(i.get("latitude", 0))
		i["longitude"] = float(i.get("longitude", 0))
	
	return mushroomList
