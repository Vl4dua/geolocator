import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from myphone import number
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
import os

# Parsing the phone number
check_number = phonenumbers.parse(number, "GB")
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)
location = geocoder.description_for_number(check_number, "en")

# Getting the carrier
operator = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(operator, "it"))

# Getting the timezone
timezone_info = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(timezone_info))

# Geocoding the location
key = ""
geocoder = OpenCageGeocode(key)
query = str(location)
coordinate = geocoder.geocode(query)
print(coordinate)

# Getting latitude and longitude
latitude = coordinate[0]["geometry"]["lat"]
longitude = coordinate[0]["geometry"]["lng"]
print(latitude, longitude)

# Creating the map
map = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=location).add_to(map)

# Determining the desktop path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
map_path = os.path.join(desktop, "mappa.html")

# Saving the map to the desktop
map.save(map_path)
print(f"Map saved to {map_path}")
