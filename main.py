from api.getObservation import getObservation
from objects.mushroom import Mushroom, MushroomList
from dash import Dash, html, dash_table, callback, Output, Input , dcc
import plotly.express as px
import pandas as pd
import numpy as np

def parseMushroomList():
	mushroomList = getObservation()
	porcinis = MushroomList(mushroomList)
	return porcinis
	
app = Dash()
porcinis = parseMushroomList()
#convert porcinis from mushroom objects to dictionary entries
mushroomData = [mush.to_dict() for mush in porcinis.getAll()]

df = pd.DataFrame(mushroomData)
months = np.arange(1,12)
centre = {
	"lat": df["latitude"].mean(),
	"lon": df["longitude"].mean()
}
#print(porcinis.getSize())

## dash app layout
app.layout = [
	html.H2(children="Porcini Geo"),
	html.Div(
		dcc.Graph(id='mapFig'),
		style={"width":"80%", "margin":"auto"}
	),
	html.Div(
		dcc.Slider(id='monthSlider',min=1,max=12,step=1,value=6,marks={i: str(i) for i in range(1,13)},tooltip={"placement":"bottom","always_visible":True}),
    	style={"width":"80%", "margin":"auto"}
	),
	dash_table.DataTable(data=mushroomData, page_size=10)
]

## TODO could be worth putting all but filtering logic in a function in a separate file
## app outputs : mapFig, return type scatter map
## app inputs : monthSlider, type (dash) dccSlider
@app.callback(
      Output("mapFig", "figure"),
      Input("monthSlider","value")
)
def update_map(curMonth):
	monthDf = df[df["month"] == curMonth]
	mapFig = px.scatter_map(
		monthDf,
		lat="latitude",
		lon="longitude",
		hover_name="place",
		hover_data=["month"],
		center=centre,
		color_discrete_sequence=["green"],
		zoom=5,
		height=600
	)

	mapFig.update_layout(mapbox_style="open-street-map")
	mapFig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
	return mapFig

if __name__ == "__main__":
    app.run(debug=True)