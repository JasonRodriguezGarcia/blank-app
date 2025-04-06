import streamlit as st
import datetime
import time
import pandas as pd
import frases_dia
import os

fichero = "datos.csv"

# datos iniciales de ejemplo
# data = {
#     'Date': ['2025-06-01', '2025-06-02', '2025-06-05'],
#     'SugarIndex': [120, 130, 125],
#     'Steps': [1000, 1200, 950],
#     'Intensity': ["Slow", "Moderate", "Fast"],
#     'Time': [1.50, 2.00, 2.20],
#     'Weight': [55.50, 55.00, 55.20]
# }
# df = pd.DataFrame(data)

comidasCenas = ["Ninguna", "Arroz", "Carne", "Huevos", "Legumbre", "Otros", "Pasta", "Pescado", "Verdura"]
campos = [ 'Fecha', 'Salsa', 'Enfriado', 'Nerviosa', 'Caminado', 'Regla', 'Migrana', 'Comido', 'BebidaComida', 'Merendado',
            'Cenado', 'BebidaCena', 'Resultado', 'FechaAyer' ]

# lógica para manejar con session_state
# if 'dataRosa' not in st.session_state:
#     df = pd.DataFrame(columns=['Fecha',  'Salsa', 'Enfriado', 'Caminado', 'Regla', "Migraña",
#                                 'Comido', 'BebidaComida', 'Merendado', 'Cenado', 'BebidaCena',
#                                 'Resultado', "FechaAyer"])

# else:
#     df = st.session_state['dataRosa']

st.subheader("Datos Rosa", divider=True)
st.write(frases_dia.frase())

# comprobación de si el fichero de datos existe
if os.path.exists(fichero):
    # Leer el archivo CSV
    df = pd.read_csv(fichero, encoding='utf-8')
    # st.write("Datos cargados correctamente:", df)
else:

    # Crear un DataFrame vacío o con datos predeterminados
    # ojo al meter datos iniciales no usamos "columns=", sino un objeto con los campos y datos por defecto
    df = pd.DataFrame(columns = (campos))
    #     'Fecha': ["2025-1-2"], 'Salsa': ['ninguna'], 'Enfriado': ['No'], 'Caminado': ['No'], 'Regla': ['No'], "Migraña": ['No'],
    #     'Comido': ['Ninguna'], 'BebidaComida': ['Agua'], 'Merendado': [''], 'Cenado': ['ninguna'], 'BebidaCena': ['No'],
    #     'Resultado': ['Bien'], "FechaAyer": [2025-1-1]
    # })
    
    # añadiendo 1º un registro con datos iniciales
    data_new = {
        'Fecha': datetime.datetime(2025, 1, 2, 0, 0, 0), 'Salsa': 'Ninguna', 'Enfriado': 'No', 'Nerviosa': 'No', 'Caminado': 'No', 'Regla': 'No', "Migrana": 'No',
        'Comido': 'Ninguna', 'BebidaComida': 'Agua', 'Merendado': '', 'Cenado': 'Ninguna', 'BebidaCena': 'Agua',
        'Resultado': 'Bien', "FechaAyer": datetime.datetime(2025, 1, 1, 0, 0, 0)
    }
    df.loc[len(df)] = data_new
    # Guardar el DataFrame vacío como CSV
    df.to_csv(fichero, date_format='%Y-%m-%d %H:%M:%S', index=False)

with st.form("my_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)

    with col1:

        dateLog = st.date_input(
            "Fecha:",
            datetime.datetime.now(),
            format="DD/MM/YYYY",
            min_value=datetime.date(2020, 1, 1),
            max_value=datetime.date(2050, 1, 1)
        )
        # pesoLog = st.number_input("Peso Kgs:",
        #     min_value=40.000,
        #     max_value=200.000,
        #     value=130.000,
        #     step=0.1,
        #     format="%0.1f"
        # )

    with col2:
        salsaLog = st.selectbox("Salsa", ["Ninguna", "Alioli", "Mahonesa", "Picante"], index=0)
        enfriadoLog = st.selectbox("Enfriado", ["Si", "No"], index=1)
        nerviosaLog = st.selectbox("Nerviosa", ["Si", "No"], index=1)
        caminadoLog = st.selectbox("Caminado", ["Si", "No"], index=1)
        reglaLog = st.selectbox("Regla", ["Si", "No"], index=1)
        migranaLog = st.selectbox("Migraña", ["Si", "No"], index=1)
    with col3:
        comidoLog = st.selectbox("Comida", comidasCenas, index=0)
        bebidaComidaLog = st.selectbox("Bebida comida", ["Agua", "Vino", "Cerveza", "Kalimotxo", "Agua"], index=0)
        merendadoLog = st.text_input("Merendado")
        cenadoLog = st.selectbox("Cena", comidasCenas, index=0)
        bebidaCenaLog = st.selectbox("Bebida cena", ["Agua", "Vino", "Cerveza", "Kalimotxo", "Agua"], index=0)

    col1b, col2b, col3b = st.columns(3)

    with col1b:
        dateAyerLog = dateLog - datetime.timedelta(days=1)
        st.write("Fecha dia anterior")
        st.text(dateAyerLog.strftime("%d/%m/%Y"))

    with col2b:
        resultadoLog = st.selectbox("Resultado", ["Bien", "Mal"], index=0)
    
    with col3b:
        st.write(" ")

    if st.form_submit_button("Save"):
        with st.spinner("Saving data ...", show_time=True):
            data_new = {
                'Fecha': pd.to_datetime(dateLog),
                'Salsa': salsaLog,
                'Enfriado': enfriadoLog,
                'Nerviosa': nerviosaLog,
                'Caminado': caminadoLog,
                'Regla': reglaLog,
                'Migrana': migranaLog, 
                'Comido': comidoLog,
                'BebidaComida': bebidaComidaLog,
                'Merendado': merendadoLog,
                'Cenado': cenadoLog,
                'BebidaCena': bebidaCenaLog,
                'Resultado': resultadoLog,
                'FechaAyer': dateAyerLog
            }

            print(data_new)
            # También podrías cambiar varias columnas si lo deseas
# df.loc[df["Name"] == "Alice", ["Name", "Age"]] = ["Alicia", 26]
            # print("imprimo resultado del if: ", len(df.loc[df["Fecha"] == dateLog]))
            # print("type Fecha: ", type(pd.to_datetime(df["Fecha"])))
            # print("type dateLos: ", type(dateLog))

            # fechaCondicion = pd.to_datetime(df.loc[df["Fecha"] == dateLog])
            # dateLogCondicion = pd.to_datetime(dateLog)
            # df["Fecha"] = pd.to_datetime(df["Fecha"])
            # print("imprimo fechas selección: ", df.loc[0:1, ["Fecha"]])
            # print("imprimo fecha seleccionada: ", df.loc[df["Fecha"] == dateLogCondicion])
            # df.loc[df["Fecha"] == dateLog]
            print("boolean: ", 2==2)
            print("boolean fecha: ", df.loc[df["Fecha"] == dateLog])
            print("imprimo fecha dataframe: ", pd.to_datetime(df["Fecha"]))
            print("imprimo datelog: ", dateLog)
            print("imprimo condicion chunga: ", df.loc[df["Fecha"] == dateLog])
            # print("imprimo otro chungo: ", df.loc[pd.to_datetime(df["Fecha"]).dt.date == datetime.date(dateLog.year, dateLog.month, dateLog.day)])
            editando =df.loc[pd.to_datetime(df["Fecha"]).dt.date == datetime.date(dateLog.year, dateLog.month, dateLog.day)]
            print("cuantos registros tienes: ", len(editando))
            print("imprimo datelog type: ", type(dateLog))
            # print("imprimo datelog year: ", datetime.datetime.datelog.year)
            # dateLog2 = dateLog.date()
            if len(df.loc[pd.to_datetime(df["Fecha"]).dt.date == dateLog]) > 0:
                print("paso por aquí")
                # si la fecha ya existe reemplaza los datos por los nuevos
                df.loc[df["Fecha"] == dateLog, [
                    'Fecha',
                    'Salsa',
                    'Enfriado',
                    'Nerviosa',
                    'Caminado',
                    'Regla',
                    'Migrana',
                    'Comido',
                    'BebidaComida',
                    'Merendado',
                    'Cenado',
                    'BebidaCena',
                    'Resultado',
                    # 'FechaAyer'
                ]] = [
                    dateLog,
                    salsaLog,
                    enfriadoLog,
                    nerviosaLog,
                    caminadoLog,
                    reglaLog,
                    migranaLog, 
                    comidoLog,
                    bebidaComidaLog,
                    merendadoLog,
                    cenadoLog,
                    bebidaCenaLog,
                    resultadoLog,
                    # dateAyerLog
                ]
            else:
                # si la fecha no existe, es que son datos nuevos
                df.loc[len(df)] = data_new
            print("imprimo df: ", df)
            # Guardar el DataFrame en una ruta específica con opciones adicionales
            # df.to_csv('/ruta/a/tu/archivo.csv', sep=';', encoding='utf-8', index=False)
            # Guardar el DataFrame en una ruta específica con opciones adicionales
            df.to_csv('datos.csv', encoding='utf-8', index=False)
            #antigua lógica guardando a session_state
            # st.session_state['dataRosa'] = df
            st.success("Guardando datos ...")
            time.sleep(1)
        st.write("Data saved")
    # print(df)
    st.write(df)

    # antigua lógica con session_state
    # if 'dataRosa' in st.session_state:
    #     st.session_state['dataRosa']


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

