from pymongo import MongoClient
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

URI = f'mongodb+srv://guicasgar:{'contraseña'}@mongodbcluster.coqmj.mongodb.net/?retryWrites=true&w=majority&appName=MongoDBCluster'
cliente = MongoClient(URI)
bbdd = cliente.IntecssaDB
coleccion = bbdd.activar_encuesta
registro = bbdd.registro_programacion

def main():
    st.title("Administración de la encuesta")
    b1 =st.button("Activar")
    b2 =st.button("Desactivar")
    b3 = st.button("Generar informe")

    if b1:
        activar()
        st.write("Activado")
    elif b2:
        desactivar()
        st.write("Desactivado")
    elif b3:
        datos = registro.find()
        df = pd.DataFrame(list(datos))
        st.dataframe(df.iloc[:,1:])
        #conteo = df['resultado'].value_counts()
        #fig,ax = plt.subplots()
        #ax.bar(x=conteo.index,height=conteo.values)
        #st.write(fig)


def activar():
    coleccion.update_one({'active':0},
                           {'$set':{'active':1}})        
    
def desactivar():
    coleccion.update_one({'active':1},
                           {'$set':{'active':0}})
    
main()