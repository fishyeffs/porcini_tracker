import requests, json

def getObservation():
	params = {
		"taxon_id" : 48701,
		"iconic_taxa" : "Fungi",
		"per_page" : 30,
		"place_id" : 6857
	}

	response = requests.get("https://inaturalist.org./observations.json", params)
	mushroomList = response.json()
	print("HTTP Response: ", response.status_code)

	#print(json.dumps(mushroomList, indent=2))

	return mushroomList
