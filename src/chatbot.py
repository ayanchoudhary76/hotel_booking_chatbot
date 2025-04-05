# src/chatbot.py

def respond_to_user_input(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    hotel_keywords = ["hotel", "hotels", "stay", "accommodation"]

    if any(greet in user_input for greet in greetings):
        return "Hello! 👋 How can I assist you today?"

    elif any(word in user_input for word in hotel_keywords):
        # Extract city name - simple assumption-based extraction
        # e.g., "show me hotels in Delhi"
        tokens = user_input.split()
        if "in" in tokens:
            city_index = tokens.index("in") + 1
            if city_index < len(tokens):
                city = tokens[city_index]
                return {"action": "search_hotels", "city": city}
            else:
                return "❌ I couldn't find the city name in your input. Please try again."
        else:
            return "🔍 Please specify the city like 'hotels in Mumbai'"

    else:
        return "🤖 I'm sorry, I didn't understand that. You can say something like 'show me hotels in Goa'."
