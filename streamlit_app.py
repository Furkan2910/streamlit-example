import streamlit as st

# Seitentitel und Beschreibung
st.title('ScrumBuddy: KI-gestützter Story Points Schätzer')
st.write("Willkommen beim ScrumBuddy, Ihrem intelligenten Assistenten für die Schätzung von Story Points. Integrieren Sie nahtlos in Jira, um Ihre Planungssitzungen zu optimieren.")

# Benutzereingaben
st.header('User Story Details')
user_story = st.text_area("Geben Sie die Beschreibung der User Story ein:", height=150)
team_experience = st.slider("Bewerten Sie die Erfahrung des Teams (1-10):", 1, 10, 5)

# Platzhalter für die Schätzung und das Reasoning
estimated_points_placeholder = st.empty()
reasoning_placeholder = st.empty()

# Schätzbutton
if st.button('Schätzen'):
    # Hier würde die Logik zur Schätzung der Story Points stehen
    # Dies ist nur ein Platzhalterwert. Ersetze ihn durch den Aufruf deines Modells
    estimated_story_points = 42  # Beispielwert
    reasoning = "Basierend auf der Teamerfahrung und der Komplexität der User Story."

    # Anzeigen der Schätzung und des Reasonings
    estimated_points_placeholder.subheader(f"### Geschätzte Story Points: {estimated_story_points}")
    reasoning_placeholder.write(f"#### Begründung: {reasoning}")

# Optional: Jira-Integration (Simulation)
st.header('Jira Integration (Optional)')
st.write("Um Aufgaben aus Jira zu importieren oder Schätzungen in Jira zu speichern, geben Sie Ihre Zugangsdaten ein.")

jira_user = st.text_input("Jira Benutzername")
jira_token = st.text_input("Jira API-Token", type="password")

if st.button('Verbinde mit Jira'):
    # Hier würde der Code stehen, um sich bei der Jira API anzumelden
    # Dies ist nur eine Platzhalteraktion. Ersetze sie durch deine API-Logik
    st.success('Verbunden mit Jira!')

# Hinweis für die Benutzer über den nächsten Schritt
st.info("Nachdem Sie Story Points geschätzt haben, überprüfen Sie sie im Kontext der gesamten Sprint-Planung, um eine fundierte Entscheidung zu treffen.")

# Footer
st.write("---")
st.footer("ScrumBuddy by YourCompany - Optimieren Sie Ihr Agile Management.")
