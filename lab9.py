#Saar Haber
#March 19th 2018
#lab 9

#Import the folium package for making maps
import folium

#NYC
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

#marker for hunter college
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Save the map
mapCUNY.save(outfile='nycMap.html')
