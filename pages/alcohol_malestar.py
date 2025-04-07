import streamlit as st
import datetime
import pandas as pd
import os

# longitud paso media = 0.7
# Distancia=Numero de pasos×Longitud del paso

st.subheader("Bebidas malestar", divider=True)

st.text("UNDER CONSTRUCTION ...")

fichero = "datos.csv"

if os.path.exists(fichero):
    # Leer el archivo CSV
    df = pd.read_csv(fichero, encoding='utf-8')
    st.write("Datos cargados correctamente:", df)
    print(df)
else:
    st.write ("No hay datos")

    st.line_chart(df, y=["SugarIndex", "Steps"], x="Date", y_label="Sugar Index/Steps", x_label="Date")
#     # chart_data = pd.DataFrame(df, columns=["a", "b", "c", "d", "e","f", "g"])
#     # # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#     # st.line_chart(chart_data)



# # st.session_state['data']
# if 'data' in st.session_state:
#     df = st.session_state['data']
#     print(df)
#     st.line_chart(df, y=["SugarIndex", "Steps"], x="Date", y_label="Sugar Index/Steps", x_label="Date")
#     # chart_data = pd.DataFrame(df, columns=["a", "b", "c", "d", "e","f", "g"])
#     # # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
#     # st.line_chart(chart_data)
# else:
#     st.write("No data available")

# if st.button("Save"):
#     st.write("Saving ...")
#     # st.info(f"Has pinchado {i}")
#     # st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")

