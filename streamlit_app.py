import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Laden des vorab trainierten Modells und des TF-IDF-Vektorisierers
model = joblib.load('path_to_your_trained_model.pkl')
tfidf_vectorizer = joblib.load('path_to_your_tfidf_vectorizer.pkl')

st.title('ScrumBuddy: KI-gestützter Story Points Schätzer')

# Nutzereingabe für die User Story
user_story = st.text_area("Geben Sie die Beschreibung der User Story ein:")

# Button zum Auslösen der Schätzung
if st.button('Schätzen'):
    # Verarbeitung der User Story mit TF-IDF
    processed_features = tfidf_vectorizer.transform([user_story])

    # Schätzung der Story Points
    estimated_story_points = model.predict(processed_features)

    st.write(f"### Geschätzte Story Points: {estimated_story_points[0]}")

# Beispiel für das Einpflegen eines Datensatzes, falls benötigt
uploaded_file = st.file_uploader("Laden Sie Ihren Datensatz hoch", type=['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

