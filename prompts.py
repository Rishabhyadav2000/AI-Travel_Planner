def input_refinement_prompt(user_input):
    return f"""The user provided the following travel query:
"{user_input}"

Refine this by asking for missing info such as:
- Travel dates
- Destination and origin
- Preferences (food, nature, hidden gems, famous spots, etc.)
- Budget
- Accommodation and mobility needs
Respond as a helpful travel assistant.
"""

def activity_suggestion_prompt(destination, preferences):
    return f"""Suggest:
- Top 5 attractions in {destination}
- 3 food experiences
- 3 hidden or local-only gems
Tailor it to preferences: {preferences}.
Be specific and helpful to a solo traveler on a moderate budget.
"""

def itinerary_generation_prompt(refined_data, suggestions):
    return f"""Create a {refined_data.get('days', 5)}-day itinerary for:
- A solo traveler
- Location: {refined_data.get('destination')}
- Interests: {refined_data.get('preferences')}
- Budget: {refined_data.get('budget')}

Use these suggestions:
{suggestions}

Group locations logically. Include estimated time and local food options.
"""
