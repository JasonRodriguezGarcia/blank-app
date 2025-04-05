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

if 'dataRosa' not in st.session_state:
    df = pd.DataFrame(columns=['Fecha', 'Resultado', 'Peso', 'Salsa', 'Enfriado', 'Caminado',
                                'Comido', 'BebidaComida', 'Merendado', 'Cenado', 'BebidaCena'])

else:
    df = st.session_state['dataRosa']
# df = st.session_state['data']

# print(df)
st.subheader("Datos Rosa", divider=True)

with st.form("my_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        dateLog = st.date_input(
            "Fecha:",
            datetime.datetime.now(),
            # format="DD/MM/YYYY",
            min_value=datetime.date(2020, 1, 1),
            max_value=datetime.date(2050, 1, 1)
        )
        resultadoLog = st.selectbox("Resultado", ["Bien", "Mal"], index=0)
        pesoLog = st.number_input("Peso Kgs:",
            min_value=40.000,
            max_value=200.000,
            value=130.000,
            step=0.1,
            format="%0.1f"
        )

    with col2:
        salsaLog = st.selectbox("Salsa", ["Ninguna", "Alioli", "Mahonesa", "Picante"], index=0)
        enfriadoLog = st.selectbox("Enfriado", ["Si", "No"], index=1)
        nerviosaLog = st.selectbox("Nerviosa", ["Si", "No"], index=1)
        caminadoLog = st.selectbox("Caminado", ["Si", "No"], index=1)
    with col3:
        comidoLog = st.selectbox("Comida", ["Arroz", "Carne", "Legumbre", "Otros", "Pasta", "Pescado", "Verdura"], index=1)
        bebidaComidaLog = st.selectbox("Bebida comida", ["Vino", "Cerveza", "Kalimotxo", "Agua"], index=1)
        merendadoLog = st.text_input("Merendado")
        cenadoLog = st.selectbox("Cena", ["Arroz", "Carne", "Legumbre", "Otros", "Pasta", "Pescado", "Verdura"], index=1)
        bebidaCenaLog = st.selectbox("Bebida cena", ["Vino", "Cerveza", "Kalimotxo", "Agua"], index=1)








    if st.form_submit_button("Save"):
        with st.spinner("Saving data ...", show_time=True):
            data_new = {
                'Fecha': dateLog,
                'Resultado': resultadoLog,
                'Peso': pesoLog,
                'Salsa': salsaLog,
                'Enfriado': enfriadoLog,
                'Caminado': caminadoLog,
                'Comido': comidoLog,
                'BebidaComida': bebidaComidaLog,
                'Merendado': merendadoLog,
                'Cenado': cenadoLog,
                'BebidaCena': bebidaCenaLog
            }
            df.loc[len(df)] = data_new
            print("imprimo df: ", df)
            st.session_state['dataRosa'] = df
            # st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([data_new])], ignore_index=True)
            st.success("Dato guardado")
            time.sleep(2)
        st.write("Data saved")

if 'dataRosa' in st.session_state:
    st.session_state['dataRosa']
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