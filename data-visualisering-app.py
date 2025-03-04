import streamlit as st
import os

st.title("📊 Interaktive Analyser")

# Funktion til at vise en HTML-fil i Streamlit
def vis_html(filnavn):
    filsti = os.path.join(os.getcwd(), filnavn)  # Finder den korrekte filsti
    if os.path.exists(filsti):  # Tjekker om filen findes
        with open(filsti, "r", encoding="utf-8") as f:
            html_kode = f.read()
        st.components.v1.html(html_kode, height=600, scrolling=True)
    else:
        st.error(f"Filen {filnavn} blev ikke fundet!")

# Sidebar til at vælge analyse
option = st.sidebar.selectbox(
    "🔍 Vælg en analyse:",
    [
        "📈 Arrangør Omsætning vs. Deltagere",
        "💰 Kundenavn vs. SUM",
        "📊 Abonnement vs. Kundenavn",
        "💸 Vores Gebyr vs. Arrangør",
        "📌 Gebyr Kategorier",
        "👥 Deltagere vs. Arrangør"
    ]
)

# Viser den valgte HTML-fil
if option == "📈 Arrangør Omsætning vs. Deltagere":
    vis_html("arrangor_oms_vs_deltagere.html")
elif option == "💰 Kundenavn vs. SUM":
    vis_html("kundenavn_vs_sum.html")
elif option == "📊 Abonnement vs. Kundenavn":
    vis_html("abonnement_vs_kundenavn.html")
elif option == "💸 Vores Gebyr vs. Arrangør":
    vis_html("vores_gebyr_vs_arrangor.html")
elif option == "📌 Gebyr Kategorier":
    vis_html("gebyr_categories.html")
elif option == "👥 Deltagere vs. Arrangør":
    vis_html("deltagere_vs_arrangor_med_median.html")
