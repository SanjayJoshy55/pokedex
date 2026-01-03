import streamlit as st
import json
import os

st.set_page_config(
    page_title="HoennDex Web",
    page_icon="🔴",
    layout="wide"
)

st.title("🔴 Pokémon Omega Ruby Companion")

st.markdown("""
Welcome to **HoennDex Web**! Your ultimate companion for the Hoenn Region.
Navigate using the sidebar to view the Pokedex or check out Secrets.
""")

# --- Rotom Guide Chatbot ---
st.header("⚡ Rotom Guide")
st.caption("Ask me about Gym locations, HMs, or Key Items!")

# Load Knowledge Base
@st.cache_data
def load_locations():
    path = os.path.join("data", "locations.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

locations = load_locations()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Zzzzt! I am Rotom! Ask me where anything is in Hoenn!"}
    ]

# Display Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat Input
if prompt := st.chat_input("Where is the Move Deleter?"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Bot Logic
    response = "Zzzzt? I don't have that in my database yet. Try asking about a Gym, HM, or specific Key Item."
    
    prompt_lower = prompt.lower()
    found = False
    
    # Simple search in our knowledge base
    # Flatten structure for easier search
    all_locations = {}
    for category in locations.values():
        all_locations.update(category)
        
    for key, value in all_locations.items():
        if key.lower() in prompt_lower:
            response = f"**{key}**: {value}"
            found = True
            break
            
    # Add to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
