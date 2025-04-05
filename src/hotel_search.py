import requests

def search_hotels(lat, lng, rapidapi_key, rapidapi_host):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": rapidapi_host
    }
    params = {
        "latitude": lat,
        "longitude": lng,
        "checkin_date": "2025-04-06",
        "checkout_date": "2025-04-07",
        "adults_number": 2,
        "room_number": 1,
        "order_by": "price",
        "locale": "en-gb",
        "currency": "INR",
        "filter_by_currency": "INR",
        "units": "metric"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()