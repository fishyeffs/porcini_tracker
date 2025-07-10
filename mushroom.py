import re

class Mushroom:
	def __init__(self, place, creation_time, latitude, longitude):
		self.place = place
		self.creation_time = creation_time
		self.latitude = latitude
		self.longitude = longitude
		pattern = r"-(?P<month>[0-9]{2})-"
		reMatch = re.search(pattern, creation_time)
		self.month = reMatch.group("month")
	

class MushroomList:
	def __init__(self, mushroomList):
		self.mushrooms = []
		for i in mushroomList:
			#print(f'{i["place_guess"]} on {i["created_at"]} | LAT: {i["latitude"]} LONG: {i["longitude"]}')
			mush = Mushroom(i["place_guess"], i["created_at"], i["latitude"], i["longitude"])
			self.addMushroom(mush)


	def addMushroom(self, mushroom):
		self.mushrooms.append(mushroom)

	def getAll(self):
		return self.mushrooms

	def get(self, index):
		return self.mushrooms[index]

	def __len__(self):
		return len(self.mushrooms)