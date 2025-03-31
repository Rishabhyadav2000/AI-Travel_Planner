def mock_refine_input(user_input):
    return {
        "destination": "Rome",
        "days": 5,
        "origin": "London",
        "preferences": "History and Food",
        "budget": "Moderate",
        "accommodation": "Budget and central",
        "mobility": "No walking issues",
        "travel_dates": "May 1–5"
    }

def mock_activity_suggestions():
    return {
        "historical": ["Colosseum", "Pantheon", "Roman Forum", "Vatican Museums", "Castel Sant'Angelo"],
        "food": ["Trastevere food tour", "Campo de' Fiori market", "Jewish Ghetto walk"],
        "hidden_gems": ["Aventine Keyhole", "Villa Celimontana", "Testaccio Market"]
    }

def generate_itinerary(data, suggestions):
    itinerary = {
        "Day 1": [
            "Arrive in Rome, check-in at central hotel",
            "Evening: Explore Trastevere and join a street food tour"
        ],
        "Day 2": [
            "Morning: Colosseum, Roman Forum",
            "Afternoon: Lunch at Campo de' Fiori",
            "Evening: Pantheon and Gelato near Trevi Fountain"
        ],
        "Day 3": [
            "Morning: Vatican Museums, St. Peter’s Basilica",
            "Afternoon: Pizza lunch, explore Castel Sant’Angelo",
            "Evening: Stroll along Tiber River"
        ],
        "Day 4": [
            "Morning: Aventine Keyhole, Orange Garden",
            "Afternoon: Testaccio food market",
            "Evening: Villa Celimontana for sunset"
        ],
        "Day 5": [
            "Morning: Espresso bar crawl",
            "Relax near Piazza Navona",
            "Departure"
        ]
    }
    return itinerary
