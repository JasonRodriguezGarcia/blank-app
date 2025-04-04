import streamlit as st
import time

PATH = "./pages/"
st.title("Health care")

# st.write("Instrucciones")

# page = st.sidebar.selectbox("Choose a peich", ["Otro", "Home", "Page 1"])

# fecha
# pasos
# intensidad
# tiempo
# peso
# distancia (calculado)
# calorías (calculado)
# indice 

pages = {
    "Home": [
        st.Page(PATH + "home.py", title="Home"),
    ],
    "Data entry": [
        st.Page(PATH + "data_entry.py", title="Data entry"),
    ],
    "Statistics": [
        st.Page(PATH + "calories_consumed.py", title="Calories consumed"),
        st.Page(PATH + "distance_travelled.py", title="Distance travelled"),
        st.Page(PATH + "blood_sugar.py", title="Blood sugar index"),
    ],
    # "Your account": [
    #     st.Page(PATH + "create_account.py", title="Create your account"),
    #     st.Page(PATH + "manage_account.py", title="Manage your account"),        
    # ],
    # "Your account": [
    #     st.Page(PATH + "create_account.py", title="Create your account"),
    #     st.Page(PATH + "manage_account.py", title="Manage your account"),        
    # ],
    "Your account": [
        st.Page(PATH + "create_account.py", title="Create your account"),
        st.Page(PATH + "login.py", title="Login"),        
        st.Page(PATH + "manage_account.py", title="Manage your account"),        
    ],
    "Resources": [
        st.Page(PATH + "about.py", title="About us"),
        st.Page(PATH + "tryit.py", title="Try it out"),        
    ]
}

# if page == "Home":
#     mostrar_home()
# elif page == "Page 1":
#     pass
#     # mostrar_pagina1()
# else:
#     st.write("página no encontrada")

pg = st.navigation(pages)
pg.run()