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

comidasCenas = ["Ninguna", "Arroz", "Carne", "Huevos", "Legumbre", "Otros", "Pasta", "Pescado", "Verdura"]

if 'dataRosa' not in st.session_state:
    df = pd.DataFrame(columns=['Fecha',  'Salsa', 'Enfriado', 'Caminado', 'Regla', "Migraña",
                                'Comido', 'BebidaComida', 'Merendado', 'Cenado', 'BebidaCena',
                                'Resultado', "FechaAyer"])

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
        # dateAyerLog = datetime.date(dateLog.year, dateLog.month, dateLog.day-1)
            # format="DD/MM/YYYY",
        st.write("Fecha dia anterior")
        st.text(dateAyerLog.strftime("%d/%m/%Y"))

    with col2b:
        resultadoLog = st.selectbox("Resultado", ["Bien", "Mal"], index=0)
    
    with col3b:
        st.write(" ")

    if st.form_submit_button("Save"):
        with st.spinner("Saving data ...", show_time=True):
            data_new = {
                'Fecha': dateLog,
                'Salsa': salsaLog,
                'Enfriado': enfriadoLog,
                'Nerviosa': nerviosaLog,
                'Caminado': caminadoLog,
                'Regla': reglaLog,
                'Migraña': migranaLog, 
                'Comido': comidoLog,
                'BebidaComida': bebidaComidaLog,
                'Merendado': merendadoLog,
                'Cenado': cenadoLog,
                'BebidaCena': bebidaCenaLog,
                'Resultado': resultadoLog,
                'FechaAyer': dateAyerLog
            }
            df.loc[len(df)] = data_new
            print("imprimo df: ", df)
            st.session_state['dataRosa'] = df
            # st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([data_new])], ignore_index=True)
            st.success("Dato guardado")
            time.sleep(1)
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
La puerta de mi corazón se abre hacia dentro. Paso del rencor al Amor.
Hoy escucho mis sentimientos y soy amable conmigo mismo. Sé que todos mis sentimientos son mis amigos
El pasado ha terminado, ya no tiene poder en el presente. Los pensamientos de Este Momento crean mi futuro.
No es divertido ser una victima. Rechazo volver a sentirme una persona indefensa.
Reclamo mi fuerza.
Me concedo el don de librarme del pasado y me adentro con júbilo en el Ahora.
Consigo la ayuda que necesito, y ésta puede llegar de cualquier parte. Mi sistema de apoyo es sólido y afectuoso a la vez.
No hay problema, ni demasiado grande ni demasiado pequeño, que el amor no pueda resolver.
Estoy dispuesto a curarme. Estoy dispuesto a perdonar. Todo está bien.
Cuando cometo una equivocación, me doy cuenta que no es más que una parte de mi proceso de aprendizaje.
Paso del perdón a la comprensión y siento compasión por todos.
Cada día me ofrece una nueva oportunidad. El ayer ya ha concluido. Hoy es el primer día de mi futuro.
Sé que los viejos patrones negativos ya no me limitan. Me despojo de ellos sin esfuerzo.
Soy capaz de perdonar; soy afable. afectuoso y amable, y sé que la Vida me ama.
Al perdonarme a mí mismo me resulta más fácil perdonar a los demás.
Amo y acepto a todos los miembros de mi familia tal como son ahora mismo.
Me perdono por no ser una persona perfecta. Vivo de la mejor manera que sé.
No puedo cambiar a otras personas. Dejo a los demás ser como son y simplemente me amo tal como soy.
Me libero en este momento de todos los traumas de mi infancia y vivo en el amor-
Sé que no me puedo responsabilizar de otras personas. Todos estamos bajo la ley de nuestra propia conciencia.
Todas las personas tienen algo que enseñarme. Hay un propósito para que estemos juntos.
Perdono a todas las personas de mi pasado que me han infligido algún daño. Las libero con amor.
Todos los cambios que tengo ante mí en la vida son positivos.frases Louise Hay
Abandono todo el miedo y la duda; la vida se vuelve sencilla y fácil para mí.
Creo un mundo libre de estrés para mí
Soy una persona capaz y puedo hacer frente a cualquier cosa.
Me siento seguro cuando expreso mis sentimientos. Puedo estar sereno en cualquier situación.
Me deshago de mis temores de la infancia. Me siento seguro, soy un ser humano con poder.
Me hallo en el proceso de hacer cambios positivos en mi vida.
Dejo ir toda la negatividad que hay en mi cuerpo y mi mente.
Estoy dispuesto a aprender. Mientras más aprendo, más evoluciono.
No importa mi edad, siempre puedo aprender y lo hago con decisión.
Poseo la fuerza para permanecer en calma ante cualquier situación.
Cierro los ojos, tengo pensamientos positivos e inhalo y exhalo bondad.
Me amo tal y como soy, ya no aspiro a ser perfecto para amarme.
El mejor regalo que puedo hacerme es mi amor incondicional.
Tengo la autoestima, el poder y la confianza suficientes para avanzar en la vida sin dificultad
Elijo sentirme bien respecto a mí mismo. Me merezco mi amor.
No importa lo que digan o hagan los demás. #Lo que importa es cómo elijo reaccionar y lo que elijo creer acerca de  mí mismo.
Estoy dispuesto a deshacerme de cualquier necesidad de lucha o sufrimiento. Merezco todo lo bueno.
Hoy, ninguna persona, lugar o cosa puede irritarme o enojarme. Elijo estar en paz.
Mi conciencia está llena de pensamientos saludables, positivos y amorosos que se reflejan en mi experiencia.
Avanzo en la vida, sé que estoy a salvo y que cuento con la protección y guía Divina.
Expreso gratitud por todo el bien de mi vida. #Cada día me aporta maravillosas sorpresas nuevas.
Cuanto más agradecido estoy por la riqueza y abundancia en mi vida, más razones tengo para estarlo.
La abundancia fluye libremente a través de mí. Merezco lo mejor y acepto lo mejor ahora.
La vida satisface todas mis necesidades en abundancia. Confío en la Vida.
Sé que puedo hacer Milagros en mi Vida.
Mi corazón es el centro de mi poder. Sigo a mi corazón.
Me siento seguro y realizado en todo lo que hago.
Comienza hoy mismo a hablarte con amor y a vibrar en sintonía con un Universo deseoso de regalarte