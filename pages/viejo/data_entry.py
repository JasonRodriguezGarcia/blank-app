import streamlit as st
import datetime
import time
import pandas as pd


# data = {
#     'Date': ['2025-06-01', '2025-06-02', '2025-06-05'],
#     'SugarIndex': [120, 130, 125],
#     'Steps': [1000, 1200, 950],
#     'Intensity': ["Slow", "Moderate", "Fast"],
#     'Time': [1.50, 2.00, 2.20],
#     'Weight': [55.50, 55.00, 55.20]
# }
# df = pd.DataFrame(data)

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Date', 'SugarIndex', 'Steps', 'Intensity', 'Time', 'Weight'])
# else:
#     df = st.session_state['data']
# df = st.session_state['data']

# print(df)
st.subheader("Data entry", divider=True)

with st.form("my_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        dateLog = st.date_input("Date:", datetime.date(2025, 4, 1))
        sugarIndexLog = st.number_input("Blood sugar index:", min_value=100, max_value=500, value=100)

    with col2:
        stepsLog = st.number_input("Steps nr.:", min_value=1, max_value=1000000, value=1)
        intensityLog = st.selectbox("Select exercise intensity", ["Slow", "Moderate", "Fast"], index=1)

    with col3:
        timeLog = st.number_input("Time (hours):", min_value=0.01, max_value = 48.00, value=0.01, step=0.01)
        weightLog = st.number_input("Weight (kgs):", min_value=10.000, max_value=500.000, value=10.000, step=0.001)


    if st.form_submit_button("Save"):
        with st.spinner("Saving data ...", show_time=True):
            data_new = {
                'Date': dateLog,
                'SugarIndex': sugarIndexLog,
                'Steps': stepsLog,
                'Intensity': intensityLog,
                'Time': timeLog,
                'Weight': weightLog
            }
            # df.loc[len(st.session_state['data'] )] = data_new
            st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([data_new])], ignore_index=True)
            st.success("Dato guardado")
            time.sleep(2)
        st.write("Data saved")

if 'data' in st.session_state:
    st.session_state['data']
# df # printing


    # st.info(f"Has pinchado {i}")
    # st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")


# user_input = st.text_input("Ingresa tu nombre:")


# st.markdown("# Conversión de temperaturas")
# dato = st.text_input("Introduce número:")

# # Crear botón para calcular
# accion = st.selectbox("Convertir a:", ["Celcius", "Farenheit"])

# if st.button("Calcular"): # button onclick con texto "Calcular" haz ...
#     dato = int(dato)

#     if accion == "Celcius":
#         conversion = (dato - 32) * (5/9)
#     elif accion == "Farenheit":
#         conversion = dato * (9/5) + 32
#     else:
#         conversion = "opción no válida"

#     st.write(f"Resultado final es: {conversion}!")

# on = st.toggle("Activar botones")

# if on:
#     # st.write("Feature activated!")

#     for i in range(3):
#         if st.button(str(i)):
#             st.info(f"Has pinchado {i}")
#             st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")