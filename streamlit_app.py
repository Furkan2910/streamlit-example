import streamlit as st

# Festlegung eines Farbschemas und weiterer Designparameter, die zu Jira passen
primaryColor="#0E8A16"  # Dunkelgrün, ähnlich dem Jira Grün
backgroundColor="#F0F2F6"  # Helles Grau für den Hintergrund, ähnlich Jira's Hintergrund
secondaryBackgroundColor="#FFFFFF"  # Weiß für Sekundärkästen
textColor="#262730"  # Fast Schwarz für Texte
font="sans serif"

# Anpassung des Streamlit-Layouts
st.set_page_config(
    page_title='ScrumBuddy - Story Points Schätzer',
    layout='wide',
    initial_sidebar_state='expanded',
    page_icon=':memo:',
    menu_items={
        'Get Help': 'https://www.atlassian.com/software/jira',
        'Report a bug': "https://www.atlassian.com/software/jira/contact",
        'About': "# ScrumBuddy: Integriertes Tool für agile Schätzungen"
    }
)

# Seitentitel und Beschreibung
st.title('ScrumBuddy: KI-gestützter Story Points Schätzer')
st.markdown("## Nahtlos integriert mit Ihrer Jira-Umgebung")
st.markdown("### Geben Sie Details zu Ihrer User Story ein und erhalten Sie sofortige Schätzungen.")

# Zwei Spalten für das Eingabeformular und die Ergebnisse
col1, col2 = st.beta_columns(2)

with col1:
    st.subheader('User Story Beschreibung:')
    user_story = st.text_area("", height=150, help="Beschreiben Sie die Aufgabe, die geschätzt werden soll.")

with col2:
    st.subheader('Ergebnisse:')
    estimated_story_points_placeholder = st.empty()
    reasoning_placeholder = st.empty()

# Schätzbutton
if st.button('Story Points Schätzen'):
    # Hier würde die Logik zur Schätzung der Story Points stehen
    estimated_story_points = "5"  # Beispielwert, ersetze ihn durch die Modellausgabe
    reasoning = "Diese Story wurde aufgrund ihrer Komplexität und des erforderlichen Aufwands als mittelgroß eingestuft."

    # Anzeige der Schätzung und der Begründung im zweiten Spaltenblock
    with col2:
        estimated_story_points_placeholder.subheader(f"**Geschätzte Story Points**: {estimated_story_points}")
        reasoning_placeholder.info(f"**Begründung**: {reasoning}")

# Optional: Verlinkungen zu Jira, falls eine tiefere Integration gewünscht ist
st.markdown("#### Weiterführende Schritte")
st.markdown("Überprüfen und verfeinern Sie Ihre Schätzungen in Jira oder starten Sie eine neue Sprint-Planung.")

# Hinweis für die Benutzer
st.info("Vergleichen Sie die geschätzten Story Points mit historischen Daten in Jira, um eine fundierte Entscheidung zu treffen.")

# Footer
st.markdown("---")
st.markdown("ScrumBuddy by YourCompany | [Erfahren Sie mehr über Jira-Integration](https://www.atlassian.com/software/jira)")
