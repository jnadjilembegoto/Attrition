import streamlit as st
from PIL import Image
import os
#gestion des dates
from datetime import datetime
import locale

import warnings
warnings.filterwarnings('ignore')

# Titre de l'application
st.set_page_config(page_title="DETERMINANT DE L'ATTRITION DANS LES ENTREPRISES", page_icon=":brain:")

# Charger l'image#############################################
script_dir = os.path.dirname(__file__)  # Répertoire du script actuel
logo_full_path = os.path.join(script_dir, 'logo_issea.jpg')
logo = Image.open(logo_full_path)
# Afficher l'image
col1, col2 = st.columns(2)
with col1:
    st.image(logo,  use_column_width=True)
with col2:
    st.write('# US consulting attrition')


# Option pour afficher la date du jour
try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
except locale.Error:
    pass#st.warning("Locale 'fr_FR.UTF-8' non disponible. Les dates seront en anglais.")

j = datetime.now().strftime("%A")
m = datetime.now().strftime("%B")
a = datetime.now().strftime("%Y")
st.write(f"**Date du jour :** {j} {datetime.now().strftime('%d')} {m} {a}")
st.write("Veuillez fournir les renseignements sur l'employé dont vous voulez prédire l'attrition")
colonne1,colonne2,colon3=st.columns(3)
with colonne2 :
    if st.button("Entrer les identifiants de l'employé") :
        st.switch_page("pages/1_Identification.py")

