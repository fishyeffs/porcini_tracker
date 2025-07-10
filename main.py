from api.getObservation import getObservation
from mushroom import Mushroom, MushroomList

def parseMushroomList():
	mushroomList = getObservation()
	porcinis = MushroomList(mushroomList)
	return porcinis
	
porcinis = parseMushroomList()
for i in porcinis.getAll():
	print(f'{i.place} on {i.creation_time}, {i.month} | LAT: {i.latitude} LONG: {i.longitude}')
			
