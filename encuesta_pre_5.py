from pymongo import MongoClient
import pandas as pd
import streamlit as st

URI = f'mongodb+srv://guicasgar:{'contraseña'}@mongodbcluster.coqmj.mongodb.net/?retryWrites=true&w=majority&appName=MongoDBCluster'
cliente = MongoClient(URI)
bbdd = cliente.IntecssaDB
coleccion = bbdd.activar_encuesta
registro = bbdd.registro_programacion

def crear_formulario():
    with st.form(key='Mi formulario'):
        Nombre = st.text_input('Ingrese su nombre: ')
        Email = st.text_input('Ingrese su correo electrónico: ')
        Edad = st.number_input('Ingrese su edad: ', min_value=0, step=1, format="%d")
        Lenguaje = st.selectbox('Elija en el desplegable el lenguaje de programación que utilice actualmente: ', ["Python", "R", "JavaScript"])
        Años_exp = st.number_input('Ingrese con números sus años de experiencia con el lenguaje elegido: ', min_value=0, step=1, format="%d")
        Pais = st.text_input('Ingrese su país de procedencia: ')

        respuesta = dict(Nombre=Nombre, Email=Email, Edad=Edad, Lenguaje=Lenguaje, Años_exp=Años_exp, Pais=Pais)

        enviar = st.form_submit_button("Enviar") 

    if enviar:
        registro.insert_one(respuesta)

st.title('CUESTIONARIO')
encuesta = coleccion.find_one()

if encuesta['active'] == 1:
    crear_formulario()
else:
    st.write('No está activo')