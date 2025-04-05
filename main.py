import re
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from src.coordinates import get_coordinates
from src.hotel_search import search_hotels

# Load environment variables
load_dotenv()

rapidapi_key = os.getenv("RAPIDAPI_KEY")
rapidapi_host = os.getenv("RAPIDAPI_HOST")
opencage_key = os.getenv("OPENCAGE_KEY")

# Maintain context
last_city = None
last_hotels = []

def apply_filters(user_input, hotels):
    if "sort by price" in user_input:
        hotels = sorted(hotels, key=lambda x: x.get("min_total_price", float('inf')))
    elif "sort by rating" in user_input:
        hotels = sorted(hotels, key=lambda x: x.get("review_score") or 0, reverse=True)
    elif "within" in user_input:
        distance_match = re.search(r"within (\d+(\.\d+)?) ?km", user_input)
        if distance_match:
            max_distance = float(distance_match.group(1))
            hotels = [h for h in hotels if float(h.get("distance", float('inf'))) <= max_distance]
    elif "price between" in user_input:
        price_match = re.search(r"price between (\d+) and (\d+)", user_input)
        if price_match:
            min_price = float(price_match.group(1))
            max_price = float(price_match.group(2))
            hotels = [h for h in hotels if min_price <= float(h.get("min_total_price", 0)) <= max_price]
    return hotels

def get_hotel_details(user_input, hotels):
    match = re.search(r"(?:tell me more about|more details about|more about) (.+)", user_input)
    if match:
        name_query = match.group(1).strip().lower()
        for hotel in hotels:
            if name_query in hotel.get("hotel_name", "").lower():
                details = f"\U0001F3E8 {hotel.get('hotel_name', 'N/A')}\n"
                details += f"⭐ Rating: {hotel.get('review_score', 'N/A')}\n"
                price = hotel.get("min_total_price", 'N/A')
                if isinstance(price, (float, int)):
                    price = f"{price:.2f}"
                details += f"\U0001F4B8 Price: {price} {hotel.get('currencycode', '')}\n"
                details += f"\U0001F37F Type: {hotel.get('accommodation_type_name', 'N/A')}\n"
                details += f"\U0001F4CD Address: {hotel.get('address', 'N/A')}\n"
                details += f"\U0001F4CF Distance: {hotel.get('distance', 'N/A')} km\n"
                return details
    return None

def respond_to_user_input(user_input):
    global last_city, last_hotels
    user_input = user_input.lower()

    # Detect hotel query and extract city first
    city_match = re.search(r"hotels in ([a-zA-Z ]+)", user_input)
    if city_match:
        city = city_match.group(1)
        lat, lng = get_coordinates(city, opencage_key)
        if lat and lng:
            result = search_hotels(lat, lng, rapidapi_key, rapidapi_host)
            hotels = result.get("result", [])
            last_city = city
            last_hotels = hotels
            if not hotels:
                return f"Sorry, I couldn't find any hotels in {city}."

            hotels = apply_filters(user_input, hotels)
            return format_hotel_response(city, hotels)
        else:
            return f"❌ Sorry, I couldn't find the coordinates for {city}."

    # Apply filters to previous result
    if last_city and last_hotels and any(x in user_input for x in ["sort", "within", "price between"]):
        filtered = apply_filters(user_input, last_hotels)
        return format_hotel_response(last_city, filtered)

    # Check for detailed hotel query
    if last_hotels:
        details = get_hotel_details(user_input, last_hotels)
        if details:
            return details

    # Greetings after hotel query
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How may I help you with hotel booking today?"

    return "I'm sorry, I didn't understand that. You can ask me to show hotels in a city."

def format_hotel_response(city, hotels):
    top_hotels = hotels[:5]
    response = f"Here are the top {len(top_hotels)} hotels in {city.title()}\n"
    for hotel in top_hotels:
        name = hotel.get("hotel_name", "N/A")
        rating = hotel.get("review_score", "N/A")
        price = hotel.get("min_total_price", "N/A")
        currency = hotel.get("currencycode", "")
        if isinstance(price, (float, int)):
            price = f"{price:.2f}"
        response += f"\U0001F3E8 {name}\n⭐ Rating: {rating}\n\U0001F4B8 Price: {price} {currency}\n{'-'*30}\n"
    response += "\nWould you like to apply more filters? (e.g., sort by rating, within 5 km, price between 1000 and 2000)"
    return response

# Example interaction loop
if __name__ == "__main__":
    print("Welcome to HotelBot! Type your query or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = respond_to_user_input(user_input)
        print(f"Bot: {response}")
