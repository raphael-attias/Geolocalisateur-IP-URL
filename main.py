import socket
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim

url = input("Insèrez un URL ou une Ip: ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key="free")

geolocator = Nominatim(user_agent="geo_locator")
location = geolocator.geocode(response.city)

print(f"IP: {ip}")
print(f"Ville: {response.city}")
print(f"Région: {response.region}")
print(f"Pays: {response.country}")

if location:
    print(f"Adresse complète: {location.address}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
else:
    print("Impossible de récupérer les coordonnées géographiques.")
