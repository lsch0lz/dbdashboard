import requests

def get_routing(startingstation: str, destinationstation: str, datum: str, uhrzeit: str):
    time = datum + "T" + uhrzeit + "Z"
    adata = [
        ["15:01", "18:17", "ICE 7731", "2:14"],
        ["15:02", "18:17", "ICE 7732", "2:14"],
        ["15:03", "18:17", "ICE 7733", "2:14"],
        ["15:04", "18:17", "ICE 7734", "2:14"],
        ["15:05", "18:17", "ICE 7735", "2:14"],
        ["15:06", "18:17", "ICE 7736", "2:14"],
    ]
    start = requests.get("https://api.deutschebahn.com/freeplan/v1/location/" + startingstation)
    start = start.json()

    destination = requests.get("https://api.deutschebahn.com/freeplan/v1/location/" + destinationstation)
    destination = destination.json()

    url = "https://marudor.de/api/hafas/v3/tripSearch"
    obj = {"start": start[0]['id'], "destination": destination[0]['id'], "time": time}

    response = requests.post(url, data=obj)
    response_ = response.json()

    for i in range(0,6):
        routes = response_['routes'][i]
        departure_time = routes['departure']['time']
        adata[i][0] = departure_time[11:-8]
        arrival_time = routes['arrival']['time']
        adata[i][1] = arrival_time[11:-8]
        adata[i][2] = routes['segments'][0]['train']['name']
        time = routes['duration']
        #milliseconds to hours
        time = time / 3600000
        adata[i][3] = round(time, 2)

    return adata

def get_details(startingstation: str, destinationstation: str, datum: str, uhrzeit: str):
    time = datum + "T" + uhrzeit + "Z"

    bdata = []

    start = requests.get("https://api.deutschebahn.com/freeplan/v1/location/" + startingstation)
    start = start.json()

    destination = requests.get("https://api.deutschebahn.com/freeplan/v1/location/" + destinationstation)
    destination = destination.json()

    url = "https://marudor.de/api/hafas/v3/tripSearch"
    obj = {"start": start[0]['id'], "destination": destination[0]['id'], "time": time}

    response = requests.post(url, data=obj)
    response_routes = response.json()
    response_routes_ = response_routes['routes']

    # route = response_routes_[0]['segments']['stops']
    route = response_routes_[0]['segments'][0]['stops']
    for i, elem in enumerate(route):
        try:
            data = [elem['departure']['scheduledTime'][11:-8], elem['station']['title'], elem['departure']['platform']]
            bdata.append(data)
        except:
            data = [elem['arrival']['scheduledTime'][11:-8], elem['station']['title'],
                    elem['arrival']['platform']]
            bdata.append(data)

    return bdata
