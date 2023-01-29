import requests
import math
import json

MY_STATIONS = {'45 Rd & 11 St','46 Ave & 5 St','Vernon Blvd & 50 Ave','Jackson Ave & 46 Rd','45 Ave & 21 St'}

def haversine(lat1, lon1, lat2, lon2):
	R = 6371 # radius of Earth in km
	dLat = math.radians(lat2 - lat1)
	dLon = math.radians(lon2 - lon1)
	lat1 = math.radians(lat1)
	lat2 = math.radians(lat2)

	a = math.sin(dLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2)**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = R * c
	return d

def get_nearest_stations(lat, lon):
	url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
	response = requests.get(url)
	data = response.json()
	stations = data["data"]["stations"]
	distances = []
	for station in stations:
		station_lat = float(station["lat"])
		station_lon = float(station["lon"])
		distance = haversine(lat, lon, station_lat, station_lon)
		distances.append((distance, station))
	distances.sort(key=lambda x: x[0])
	return [d for d in distances[:10] if d[1]['name'] in MY_STATIONS]

# Getting the hardcode data
lat, lon = 40.74523951004758, -73.95202097950992
nearest_stations = get_nearest_stations(lat, lon)
output_dict = {}
for _, station in nearest_stations:
	output_dict[station['station_id']] = station['name']
print(json.dumps(output_dict))
