import folium
world_map=folium.Map(
    zoom_start=4,
    tiles='mapbox Bright'
)
world_geo='world_countries.json'
import pandas as pd
df_can=pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
df=df_can[['OdName','Total']]
world_map.choropleth(
    geo_data=world_geo,
    data=df,
    columns=['OdName','Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    legend_name='Immigration to Canada'
)
world_map.save('chloro.html')