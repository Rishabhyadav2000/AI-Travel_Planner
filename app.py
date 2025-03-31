import streamlit as st
from prompts import input_refinement_prompt, activity_suggestion_prompt, itinerary_generation_prompt
from itinerary_generator import mock_refine_input, mock_activity_suggestions, generate_itinerary

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("🧳 AI-Powered Travel Planner")

st.markdown("Enter your travel preferences to get a personalized travel itinerary.")

user_input = st.text_area("What are your travel goals?")

if st.button("Generate Itinerary") and user_input:
    st.subheader("🧠 Step 1: Understanding your context")
    refined_data = mock_refine_input(user_input)
    st.json(refined_data)

    st.subheader("🔍 Step 2: Finding top experiences")
    suggestions = mock_activity_suggestions()
    st.json(suggestions)

    st.subheader("📅 Step 3: Your Personalized Itinerary")
    itinerary = generate_itinerary(refined_data, suggestions)

    for day, activities in itinerary.items():
        st.markdown(f"**{day}**")
        for item in activities:
            st.markdown(f"- {item}")
        st.markdown("---")
