# 🏨 Hotel Booking Chatbot

A smart chatbot built with Python to help users discover hotels by city name. It uses OpenCage for geolocation and Booking.com’s API to fetch real-time hotel data.

## ✨ Key Features

- 🌍 **Location Detection** – Converts city names into coordinates using the OpenCage API.
- 🏘️ **Hotel Suggestions** – Finds top hotel listings with details like name, rating, and pricing via the Booking.com API.
- 💬 **Interactive Experience** – Engages with users to display relevant hotel options.

## 🚀 Getting Started

Follow these steps to run the project locally:

### 📋 Requirements

- Python 3.10 or above
- pip (Python package manager)
- (Recommended) Virtual environment tool like `venv`

### 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/ayanchoudhary76/hotel_booking_chatbot.git
   cd hotel_booking_chatbot
   ```

2. **Create a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   - Copy the sample file:

     ```bash
     cp .env.example .env
     ```

   - Replace placeholders in `.env` with your actual API keys:

     ```env
     OPENCAGE_API_KEY=your_opencage_key
     BOOKING_API_KEY=your_booking_key
     ```

### ▶️ Launch the Bot

Run the main Python script:

```bash
python main.py
```

## 🗂️ Project Layout

- `main.py` – Launches the chatbot interface.
- `src/` – Contains all core modules for geolocation, hotel search, and chatbot logic.
- `requirements.txt` – List of project dependencies.
- `.env.example` – Template for environment variables.
- `structure.txt` – Overview of the file organization.

## 🤝 Contributions

Want to make this bot better? Fork the repo, make your changes, and open a pull request. All kinds of contributions are welcome!

