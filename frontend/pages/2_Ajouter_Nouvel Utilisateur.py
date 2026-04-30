# Ajouter_Nouvel Utilisateur
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ajouter utilisateur")

st.title(" Ajouter un nouvel utilisateur")

# =========================
# 📥 Formulaire
# =========================

with st.form("user_form"):
    user_id = st.text_input("User ID")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")

    submitted = st.form_submit_button("Ajouter")

# =========================
# 💾 Sauvegarde
# =========================

if submitted:
    if user_id and nom and prenom:

        new_user = pd.DataFrame([{
            "user_id": user_id,
            "nom": nom,
            "prenom": prenom
        }])

        file_path = "users_50.csv"

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, new_user], ignore_index=True)
        else:
            df = new_user

        df.to_csv(file_path, index=False)

        st.success(f"Utilisateur {prenom} {nom} ajouté !")

        st.rerun()

    else:
        st.warning("Merci de remplir tous les champs")