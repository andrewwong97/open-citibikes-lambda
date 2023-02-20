import requests

# official station id to official station name
MY_STATIONS = {
    '3125': '45 Rd & 11 St',
    '3124': '46 Ave & 5 St',
    '3119': 'Vernon Blvd & 50 Ave',
    '3121': 'Jackson Ave & 46 Rd',
    '4674': '45 Ave & 21 St',
    '3122': '48 Ave & 5 St'
}

# official station name to shorthand name
STATION_SHORTHAND = {
    '45 Rd & 11 St': 'Court Square S',
    '46 Ave & 5 St': '4545 Center',
    'Vernon Blvd & 50 Ave': '7 Train',
    'Jackson Ave & 46 Rd': 'Trader Joes',
    '45 Ave & 21 St': 'Court Square N',
    '48 Ave & 5 St': '48th Ave'
}


def get_docks_available(station_ids):
	api_url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
	response = requests.get(api_url)
	station_statuses = response.json()["data"]["stations"]
	docks_available = {}
	for station in station_statuses:
		if station["station_id"] in station_ids:
			station_name = MY_STATIONS[station["station_id"]]
			docks_available[STATION_SHORTHAND[station_name]] = station["num_docks_available"]
	return docks_available

# Getting actual open docks
print(get_docks_available(MY_STATIONS))