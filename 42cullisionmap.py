#Saar Haber
#April 10th 2018
#program 42

import folium
import pandas as pd

#read in the CSV file. print out the campus locations 
cuny = pd.read_csv('cunyLocations.csv')
print (cuny["TIME"])
out=input('enter an outputfile nmae')
#set up a map, centered on Hunter College:
mapCUNY = folium.Map(location=[40.768731, -73.964915])

#add markers for each campus. iterate through
#the rows of dataframe to create the markers:
for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGTITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)

#save the map
mapCUNY.save(outfile=out)
