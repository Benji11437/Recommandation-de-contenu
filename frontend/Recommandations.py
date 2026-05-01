# frontend

import streamlit as st
import requests
import pandas as pd
import os

#API_URL = "http://127.0.0.1:8000/recommend"
API_URL = "https://fastapi-api-262827626932.europe-west8.run.app/recommend"

st.set_page_config(page_title="Reco Articles")

# =========================
# 🏠 PAGE PRINCIPALE
# =========================

st.markdown(
    "<h1 style='text-align: center;'>Recommandation d’articles par utilisateur</h1>",
    unsafe_allow_html=True
)

# =========================
# 🗄️ Charger users
# =========================

@st.cache_data
def load_users():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "data", "users_50.csv")

    if not os.path.exists(file_path):
        return []

    df = pd.read_csv(file_path)
    return df["user_id"].astype(int).tolist()  # ✅ int direct


user_ids = load_users()

# =========================
# 👤 Sélection user
# =========================

if len(user_ids) == 0:
    st.warning("Aucun utilisateur disponible")
    st.stop()

selected_user = st.selectbox(
    "Choisir un utilisateur",
    user_ids
)

# =========================
# 🔌 API call
# =========================

@st.cache_data
def get_recommendations(user_id):
    try:
        response = requests.get(
            API_URL,
            params={"user_id": int(user_id)},  # ✅ sécurisé
            timeout=10
        )

        if response.status_code != 200:
            return {"error": f"API error {response.status_code}"}

        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# =========================
# 🎯 Affichage
# =========================

if st.button("Afficher recommandations"):

    with st.spinner("Chargement des recommandations..."):

        data = get_recommendations(selected_user)

        #  Gestion erreur API
        if "error" in data:
            st.error(f"Erreur API : {data['error']}")
            st.stop()

        recs = data.get("recommendations", [])

        st.subheader(f"Recommandations pour {selected_user}")

        # 🔥 Cold start
        if data.get("cold_start") == "user":
            st.info("Nouvel utilisateur → recommandations populaires")

        # =========================
        # 📊 Résultats
        # =========================

        if recs:
            df = pd.DataFrame(recs[:5])
            st.dataframe(df, use_container_width=True)

            for i, article in enumerate(recs[:5], 1):
                st.markdown(f"### {i}. Article {article['article_id']}")
                st.caption(f"Score : {round(article['score'], 3)}")
                st.divider()
        else:
            st.warning("Aucune recommandation trouvée")