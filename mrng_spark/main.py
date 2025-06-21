import streamlit as st
import datetime
import random

# Motivational quotes list
quotes = [
    "Wake up with determination, go to bed with satisfaction 💪",
    "Believe in yourself, you’re halfway there 💫",
    "You are capable of amazing things 🌟",
    "Rise up. Start fresh. See the bright opportunity 🌅",
    "Push yourself, because no one else is going to do it for you 🔥"
]

# Wallpapers list (URL or local path)
wallpapers = [
    "https://wallpaperaccess.com/full/317501.jpg",
    "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",
    "https://images.unsplash.com/photo-1517180102446-f3ece451e9d8"
]

# Get today’s date
today = datetime.date.today().isoformat()

# Create or read the stored date
if "last_seen" not in st.session_state or st.session_state.last_seen != today:
    st.session_state.last_seen = today
    st.session_state.quote = random.choice(quotes)
    st.session_state.wallpaper = random.choice(wallpapers)

# Set background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("{st.session_state.wallpaper}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# App UI
st.markdown("<h1 style='text-align: center; color: white;'>✨ Mrng Spark ✨</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: white;'>💬 {st.session_state.quote}</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Made with 💛 by Sheru</p>",unsafe_allow_html=True)
            