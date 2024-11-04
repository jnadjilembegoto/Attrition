import streamlit as st
from PIL import Image
import os


script_dir = os.path.dirname(__file__)  # Répertoire du script actuel
logo_full_path = os.path.join(script_dir, 'Josi.jpg')
photo = Image.open(logo_full_path)
photo.resize((20,20))
st.title("Concepteur")
st.image(photo,use_column_width=True,caption="NADJILEM Bégoto, Ingénieur Statisticien Economiste")

#insérer des informations personnelles 
contact_info = """
    <div style='text-align: center; padding: 20px;'>
        <h4>Contactez-nous</h4>
        <p>Email: jnadjilembegoto@gmail.com</p>
        <p>Téléphone: +237681398905</p>
        <p>Adresse: Camp SIC Titigarage, B04, Rue 40, Yaoundé, Cameroun</p>
    </div>
"""
# Afficher les informations de contact en bas de la page
st.markdown(contact_info, unsafe_allow_html=True)