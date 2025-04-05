import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Step 1: Get coordinates from OpenCage
def get_coordinates(city_name, api_key):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {"q": city_name, "key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    if data["results"]:
        lat = data["results"][0]["geometry"]["lat"]
        lng = data["results"][0]["geometry"]["lng"]
        return lat, lng
    else:
        return None, None

# Step 2: Search hotels using Booking.com API
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

# Load keys from environment
OPENCAGE_KEY = os.getenv("OPENCAGE_KEY")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# Test run
city = "Goa"
lat, lng = get_coordinates(city, OPENCAGE_KEY)
if lat and lng:
    result = search_hotels(lat, lng, RAPIDAPI_KEY, RAPIDAPI_HOST)
    print("\n=== TOP 5 HOTELS ===")
    for hotel in result.get("result", [])[:5]:
        print(f"🏨 {hotel['hotel_name']}")
        print(f"⭐ Rating: {hotel.get('review_score', 'N/A')}")
        print(f"💸 Price: {hotel.get('min_total_price', 'N/A')} {hotel.get('currencycode', '')}")
        print("-" * 30)
else:
    print("❌ Could not fetch coordinates.")
