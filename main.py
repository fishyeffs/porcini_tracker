from api.getObservation import getObservation
from objects.mushroom import Mushroom, MushroomList
from dash import Dash, html, dash_table, callback, Output, Input , dcc
import plotly.express as px
import pandas as pd

def parseMushroomList():
	mushroomList = getObservation()
	porcinis = MushroomList(mushroomList)
	return porcinis
	
porcinis = parseMushroomList()
### example usage
#for i in porcinis.getAll():
#	print(f'{i.place} on {i.creation_time}, {i.month} | LAT: {i.latitude} LONG: {i.longitude}')
	

app = Dash()
porcinis = parseMushroomList()
mushroomData = [mush.to_dict() for mush in porcinis.getAll()]

df = pd.DataFrame(mushroomData)
print(porcinis.getSize())

mapFig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    hover_data=["month"],
    color_discrete_sequence=["green"],
    zoom=5,
    height=600
)

mapFig.update_layout(mapbox_style="open-street-map")
mapFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.layout = [
    html.H2(children="Porcini Geo"),
    #dash_table.DataTable(data=mushroomData, page_size=10),
    dcc.Graph(figure=mapFig),
    dcc.Slider(id='monthSlider',min=1,max=1,step=1,value=6,marks={i: str(i) for i in range(1,13)},tooltip={"placement":"bottom","always_visible":True})
]

if __name__ == "__main__":
    app.run(debug=True)