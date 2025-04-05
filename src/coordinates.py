import requests

def get_coordinates(city_name, api_key):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {"q": city_name, "key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    if data["results"]:
        lat = data["results"][0]["geometry"]["lat"]
        lng = data["results"][0]["geometry"]["lng"]
        return lat, lng
    return None, None
