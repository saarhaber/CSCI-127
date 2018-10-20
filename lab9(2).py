#Saar Haber
#April 10th 2018
#Lab 9.2

import folium
import pandas as pd

#read in the CSV file. print out the campus locations 
cuny = pd.read_csv('cunyLocations.csv')
print (cuny["Campus"])

#set up a map, centered on Hunter College:
mapCUNY = folium.Map(location=[40.768731, -73.964915])

#add markers for each campus. iterate through
#the rows of dataframe to create the markers:
for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

#save the map
mapCUNY.save(outfile='cunyLocations.html')
