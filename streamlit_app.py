import webbrowser
import streamlit as st

"""
# Hello this is a little Streamlit App!
# Hi there
"""

st.slider("I'm a slider!", 0, 10, 5)

if st.button("open google"):
    webbrowser.open("https://www.google.com")
