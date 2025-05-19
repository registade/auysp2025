
import streamlit as st
import pandas as pd

st.title("African Union Youth Startup Programme - Applications")

uploaded_file = st.file_uploader("Upload the CSV file from Google Forms", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Liste des candidatures")
    st.dataframe(df)

    countries = df["Country of Residence"].dropna().unique()
    selected_country = st.selectbox("Filtrer par pays", ["Tous"] + sorted(countries.tolist()))
    if selected_country != "Tous":
        df = df[df["Country of Residence"] == selected_country]

    selected_index = st.selectbox("Choisir une ligne à afficher en détail", range(len(df)))
    selected_row = df.iloc[selected_index]

    st.subheader("Détails de la candidature")
    for column in df.columns:
        st.markdown(f"**{column}**")
        st.write(selected_row[column])
        st.markdown("---")
else:
    st.info("Veuillez charger un fichier CSV exporté depuis Google Forms.")
