# Ajouter_Article
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ajouter article")

st.title(" Ajouter un nouvel article")

# =========================
# 📥 Formulaire
# =========================

with st.form("article_form"):
    article_id = st.text_input("Article ID")
    titre = st.text_input("Titre")
    contenu = st.text_area("Contenu")

    submitted = st.form_submit_button("Ajouter")

# =========================
# 💾 Sauvegarde
# =========================

if submitted:
    if article_id and titre and contenu:

        new_article = pd.DataFrame([{
            "article_id": article_id,
            "titre": titre,
            "contenu": contenu
        }])

        file_path = "articles.csv"

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            # 🚫 éviter doublons
            if article_id in df["article_id"].astype(str).values:
                st.error("Article déjà existant")
                st.stop()

            df = pd.concat([df, new_article], ignore_index=True)
        else:
            df = new_article

        df.to_csv(file_path, index=False)

        st.success(f"Article '{titre}' ajouté !")

        st.rerun()

    else:
        st.warning("Merci de remplir tous les champs")