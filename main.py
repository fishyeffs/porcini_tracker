from api.getObservation import getObservation
from objects.mushroom import Mushroom, MushroomList
from dash import Dash, html, dash_table, callback, Output, Input

def parseMushroomList():
	mushroomList = getObservation()
	porcinis = MushroomList(mushroomList)
	return porcinis
	
porcinis = parseMushroomList()
for i in porcinis.getAll():
	print(f'{i.place} on {i.creation_time}, {i.month} | LAT: {i.latitude} LONG: {i.longitude}')
			

app = Dash()
porcinis = parseMushroomList()
mushroomData = [mush.to_dict() for mush in porcinis.getAll()]

app.layout = [
    html.H2(children="data table"),
    dash_table.DataTable(data=mushroomData, page_size=10)
]

if __name__ == "__main__":
    app.run(debug=True)