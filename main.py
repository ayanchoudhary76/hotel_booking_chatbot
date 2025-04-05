from src.coordinates import get_coordinates
from src.hotel_search import search_hotels
from dotenv import load_dotenv
load_dotenv()
import os

# Load API keys from environment variables
OPENCAGE_KEY = os.getenv("OPENCAGE_KEY")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# Take city input from the user
city = input("Enter city name to search hotels: ").strip()

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
