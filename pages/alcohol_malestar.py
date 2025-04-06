import streamlit as st
import datetime
import pandas as pd

# longitud paso media = 0.7
# Distancia=Numero de pasos×Longitud del paso

st.subheader("Blood sugar index", divider=True)

st.text("UNDER CONSTRUCTION ...")

# st.session_state['data']
if 'data' in st.session_state:
    df = st.session_state['data']
    print(df)
    st.line_chart(df, y=["SugarIndex", "Steps"], x="Date", y_label="Sugar Index/Steps", x_label="Date")
    # chart_data = pd.DataFrame(df, columns=["a", "b", "c", "d", "e","f", "g"])
    # # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    # st.line_chart(chart_data)
else:
    st.write("No data available")

if st.button("Save"):
    st.write("Saving ...")
    # st.info(f"Has pinchado {i}")
    # st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")

