import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ajouter utilisateur")

st.title("Ajouter un nouvel utilisateur")

# 🔥 Flag de reset
if "reset_form" not in st.session_state:
    st.session_state.reset_form = False

# 🔥 Initialisation des champs (avec reset)
if st.session_state.reset_form:
    st.session_state.user_id = ""
    st.session_state.nom = ""
    st.session_state.prenom = ""
    st.session_state.reset_form = False

# =========================
# 📥 Formulaire
# =========================

with st.form("user_form"):
    user_id = st.text_input("User ID", key="user_id")
    nom = st.text_input("Nom", key="nom")
    prenom = st.text_input("Prénom", key="prenom")

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

        # 🔥 Activer le reset pour le prochain run
        st.session_state.reset_form = True

        st.rerun()

    else:
        st.warning("Merci de remplir tous les champs")