import requests
from datetime import datetime, timedelta
def search_hotels(lat, lng, rapidapi_key, rapidapi_host):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": rapidapi_host
    }

    # Dynamically set check-in and check-out dates
    today = datetime.today().strftime("%Y-%m-%d")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    params = {
        "latitude": lat,
        "longitude": lng,
        "checkin_date": today,
        "checkout_date": tomorrow,
        "adults_number": 2,
        "room_number": 1,
        "order_by": "price",
        "locale": "en-gb",
        "currency": "INR",
        "filter_by_currency": "INR",
        "units": "metric"
    }

    response = requests.get(url, headers=headers, params=params)


    if response.status_code != 200:
        return {"error": "Failed to fetch hotel details"}

    try:
        return response.json()
    except Exception as e:
        print(f"Error parsing API response: {e}")
        return {"error": "Failed to parse response"}