import streamlit as st
import pandas as pd
import openpyxl
import os
import joblib

def Info_worker ():
    st.title("Les informations sur l'employé")
    c1,c2 =st.columns(2)
    with c2:
        if st.button("Retour à l'accueil"):
            st.switch_page("Accueil.py")

    # Section 1 : Caractéristiques de l'employé
    st.header("Etat civil de l'employé")
    Age = st.number_input("Âge de l'employé", min_value=18, max_value=100, step=1, help="Entrez l'âge de l'employéé.")

    État_civil= st.radio(
        "Etat civil",
        ['Single', 'Married', 'Divorced'],
        help="Sélectionnez le statut matrimonial de l'employé"
    )

    Voyage_affaires = st.selectbox(
        "Fréquence de mission",
        [0,1,2],
        help="Fréquence à laquelle l'employé a voyagé pour le compte de l'entreprise 'Non-Travel : 0', 'Travel_Rarely : 1', 'Travel_Frequently : 2'"
    )

    DailyRate=st.number_input("Salaire horaire",help="Montant en tant que taux horaire")
    Revenu_mensuel=st.number_input("Salaire Mensuel",help="Remunération mensuelle de l'employé")
    Heures_supplémentaires=st.radio(
        "Heures supplémentaires",
        [0,1],
        help="si l'employé a effectué des heures supplémentaires ou non. 0: non 1:oui"
    )
    DistanceFromHome=st.number_input("Distance maison bureau",help="Disance entre la maison de l'emplyé et l'entreprise")
    EnvironmentSatisfaction=st.selectbox(
        "Satisfaction de l'environnement de travail",
        [1,2,3,4],
        help="une indication de la satisfaction d'un employé avec son environnement sur une échelle de 1 à 4, 1 étant « Faible », 2 « Moyen », 3 « Élevé » et 4 « Très élevé ».  "
    )

    Implication_dans_emploi=st.selectbox(
        "Implication dans l'emploi",
        [1,2,3,4],
        help="degré d'implication d'un employé dans son travail sur une échelle allant de 1 à 5. Où 1 est très peu impliqué et 5 est très impliqué. "
    )

    JobLevel=st.selectbox(
        "Niveau d'emploi",
        [1,2,3,4,5],
        help=" une indication du niveau de classement du poste d'un employé, allant de 1 à 5.1 étant un poste de bas niveau (par exemple un poste junior) et 5 un niveau de poste de haut niveau (par exemple un PDG) "
    )

    Satisfaction_travail=st.selectbox(
        "Satisfaction au travail",
        [1,2,3,4],
        help=" Niveau de satisfaction au travail "
    )
    StockOptionLevel=st.selectbox(
        "Niveau d'option d'achat",
        [0,1,2,3],
        help=" quel niveau d'option d'achat d'actions l'employé a dans l'entreprise "
    )

    TotalWorkingYears= st.number_input("Ancienneté de l'employé", min_value=0, max_value=40, step=1, help="depuis combien d'années l'employé a travaillé.") 

    TrainingTimesLastYear=st.number_input("Temps de formation de l'employé", min_value=0, max_value=100, step=1, help=" combien de temps l'employé a passé en formation l'année dernière")

    WorkLifeBalance=st.number_input("Equilibre de l'employé", min_value=1, max_value=4, step=1, help= "un indicateur de l'équilibre entre vie professionnelle et vie privée de l'employé, 1 étant « Mauvais », 2 « Bon », 3 « Excellent » et 4 « Très élevé ».")

    YearsAtCompany=st.number_input("Ancienneté de l'employé dans l'entreprise", min_value=0, max_value=100, step=1, help= "depuis combien d'années l'employé travaille dans l'entreprise")

    YearsInCurrentRole=st.number_input("Ancienneté de l'employé dans le poste", min_value=0, max_value=100, step=1,  help="depuis combien d'années l'employé occupe son poste actuel")
    YearsWithCurrManager= st.number_input("Ancienneté de l'employé avec son manager", min_value=0, max_value=100, step=1,  help="depuis combien d'années l'employé travaille avec son manager actuel.")
    Departement= st.radio(
        "Département",
        ['Sales', 'Research & Development', 'Human Resources'],
        help="Sélectionnez le département de travail de l'employé"
    )

    Education_field= st.selectbox(
        "Domaine de formation",
        ['Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree', 'Human Resources'],
        #['EducationField_Life Sciences','EducationField_Marketing','EducationField_Medical','EducationField_Other','EducationField_Technical Degree'],
        help="Dans quelle industrie l'employé a une formation"
    )
    Job_role=st.selectbox(
        "Poste",
        #['JobRole_Human Resources', 'JobRole_Laboratory Technician','JobRole_Manager', 'JobRole_Manufacturing Director','JobRole_Research Director','JobRole_Research Scientist','JobRole_Sales Executive','JobRole_Sales Representative'],
        ['Sales Executive', 'Research Scientist', 'Laboratory Technician','Manufacturing Director', 'Healthcare Representative', 'Manager','Sales Representative', 'Research Director', 'Human Resources'],
        help="intitulé du poste de l'employé"
    )
 
        # Enregistrer les données sous forme de dictionnaire
    input_data = {
            'Age':Age,
            'Voyage_affaires':Voyage_affaires,
            'DailyRate':DailyRate,
            'DistanceFromHome':DistanceFromHome,
            'EnvironmentSatisfaction':EnvironmentSatisfaction,
            'Implication_dans_emploi':Implication_dans_emploi,
            'JobLevel':JobLevel,
            'Satisfaction_travail':Satisfaction_travail,
            'Revenu_mensuel':Revenu_mensuel,
            'Heures_supplémentaires':Heures_supplémentaires,
            'StockOptionLevel':StockOptionLevel,
            'TotalWorkingYears':TotalWorkingYears,
            'TrainingTimesLastYear': TrainingTimesLastYear,
            'WorkLifeBalance': WorkLifeBalance,
            'YearsAtCompany': YearsAtCompany,
            'YearsInCurrentRole': YearsInCurrentRole,
            'YearsWithCurrManager': int(YearsWithCurrManager),
            'Department': Departement,
            'EducationField': Education_field,
            'JobRole': Job_role,
            'État_civil':État_civil,
        }
    input_df = pd.DataFrame([input_data])

    
    return input_df
    # Section 2 :
def treatInput(data):
    st.write("dummérisation en cours...")
    #importer la base de données
   # script_dir = os.path.dirname(__file__) 
    #df_full_path = os.path.join(script_dir, 'Exam_ML_ISE-2.xlsx')
    base=pd.read_excel('Exam_ML_ISE-2.xlsx',sheet_name="JeuxDeDonnées")
    base_dummy=pd.read_excel('Exam_ML_ISE-2.xlsx',sheet_name="data_dummy")
    #encodage des variables catégorielles
    dum =['Department','EducationField','JobRole','État_civil']  
    #dummérisation manuelle
    for i in dum:
        list_dum=list(base[i].unique())
        list_dum.sort()
        for j in list_dum:
          var_dum=i + "_" + j
          if var_dum in base_dummy.columns:
            data[var_dum]=0
        var_del=str(i+"_"+data[i])
        if var_del in base_dummy.columns:
            data[i+"_"+data[i]]=1
        data.drop(columns=[i],axis=1,inplace=True)
    st.success("Dummérisation effectuée avec succès!")
    return data

def prediction(data):
    treatInput(data)
    st.write("Prédiction en cours...")
    #chargement du modèle préenrégistré
    modele=joblib.load(filename="rf_model.joblib")
    attrition=modele.predict(data)
    st.success("La prédiction a été réalisée avec succès!")

    # Afficher le texte avec l'effet clignotant
    st.markdown(
    """
    <style>
    .clignotement-couleur {
        font-size: 24px;
        font-weight: bold;
        animation: couleur-clignotante 1s infinite;
    }

    @keyframes couleur-clignotante {
        0% { color: red; }
        25% { color: blue; }
        50% { color: green; }
        75% { color: orange; }
        100% { color: red; }
    }
    </style>
    """,
    unsafe_allow_html=True
    )
   
    if attrition[0]==1:
        st.markdown('<p class="clignotement-couleur">Présence d\'attrition détectée pour cet employé</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="clignotement-couleur">Absence d\'attrition prédite pour cet employé</p>', unsafe_allow_html=True)
        
    
    
##################main##########################################
input_df=Info_worker()
    # Bouton de soumission
if st.button("Soumettre les informations"):
    st.success("Les informations ont été soumises avec succès!")
    st.write("Transformation des données en DataFrame...")
    st.write(input_df)
    prediction(input_df)
