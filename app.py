import streamlit as st

######################### PAGE SETUP #########################

# Set up the page
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="wide", # or wide
    page_icon="🥝", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

######################### USER INPUT #########################

st.title("What's your superhero name?")

favourite_colour = st.text_input("", placeholder = "Enter your favourite colour:")

favourite_animal = st.text_input("", placeholder = "Enter your favourite animal:")

favourite_number = st.number_input("", placeholder = "Enter your favourite number:")

superpower = st.selectbox(
    "Select a superpower",
    ("flying", "invisibility", "super strength"),
)

if st.button("GG"):
    superhero_name = f"{favourite_colour} {favourite_animal} of {favourite_number}"
    st.header(f"Your Superhero name: {superhero_name}")
    st.write(f"Superpower: {superpower}")
