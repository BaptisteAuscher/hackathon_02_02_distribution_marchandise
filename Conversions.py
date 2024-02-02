import geopandas as gpd
from shapely.geometry import point 

data ={'Latitude':[0,1,2],'Longitude':[0,1,2]}
geometry = [point(xy) for xy in zip(data['Longitude'],data['Latitude'])]
gdf= gpd.GeoDataFrame(data, geometry=geometry)

gdf.to_file("resultats.shp",driver='ESRI Shapefile')
print(gdf)