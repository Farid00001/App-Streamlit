import streamlit as st
import pandas as pd
import plotly.express as px


st.header("INTERPRÉTATION DE DONNÉES")

file = st.file_uploader("Importer vos données ici (format CSV uniquement)", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.subheader("Aperçu des 5 premières lignes du Dataset")
    st.dataframe(df.head())  # Corrigé l'appel à `head` avec parenthèses

    st.subheader("Informations sur le Dataset")
    if st.button("Afficher les informations"):
        st.write("Nombre de colonnes :", df.shape[0])
        st.write("Nombre de ligne :", df.shape[1])
        st.write("Les colonnes du dataset sont :", list(df.columns))

    # Stats
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if not numeric_columns.empty:

        st.subheader("Graphique interactif")

        chart_type = st.radio(
            "Choisissez le type de graphique à afficher :",
            options=["Lignes (Line Chart)", "Histogramme"]
        )

        # Sélection des axes pour le graphique
        x_axis = st.selectbox("Sélectionnez une colonne pour l'axe des X", options=df.columns)
        y_axis = st.multiselect("Sélectionnez une ou plusieurs colonnes pour l'axe des Y", options=numeric_columns)
        
        if x_axis and y_axis:
            if chart_type == "Lignes (Line Chart)":
                fig = px.line(df, x=x_axis, y=y_axis, title="Graphique interactif en Lignes")
            else:
                fig = px.histogram(df, x=x_axis, y=y_axis, title="Graphique interactif Histogramme")

            st.plotly_chart(fig)
        else:
            st.warning("Veuillez sélectionner une colonne pour l'axe des X et au moins une colonne pour l'axe des Y.")
    else:
        st.warning("Aucune colonne numérique disponible pour afficher un graphique.")
else:
    st.info("Veuillez téléverser un fichier pour commencer.")
