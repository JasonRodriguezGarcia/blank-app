import streamlit as st
import time

PATH = "./pages/"
st.title("Cuida2")

pages = {
    "Home": [
        st.Page(PATH + "home.py", title="Inicio"),
    ],
    "Data entry": [
        st.Page(PATH + "data_entry_rosa.py", title="Data entry Rosa"),
    ],
    "Statistics": [
        st.Page(PATH + "alcohol_malestar.py", title="Alcohol malestar"),
    ],
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

pg = st.navigation(pages)
pg.run()