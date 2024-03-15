
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title('ScrumBuddy: KI-gestützter Story Points Schätzer')

# User input für die User Story
user_story = st.text_area("Geben Sie die Beschreibung der User Story ein:")

# Schätzbutton
if st.button('Schätzen'):
    # Hier würde die Logik zur Schätzung der Story Points stehen
    estimated_story_points = "Hier kommt die geschätzte Anzahl der Story Points hin"
    reasoning = "Hier kommt das Reasoning hinter der Schätzung hin"

    st.write(f"### Geschätzte Story Points: {estimated_story_points}")
    st.write(f"### Reasoning: {reasoning}")

