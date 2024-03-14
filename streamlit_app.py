
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

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices
x = radius * np.cos(theta)
y = radius * np.sin(theta)
df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})
st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
