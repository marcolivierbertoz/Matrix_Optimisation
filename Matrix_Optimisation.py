# Loading packages ##########################################################################
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

###############################################################################################
st.set_page_config(layout="wide")

##### Creazione Sidebar ####################################################################
st.sidebar.title('Ottimizzazione')
st.sidebar.header('Creazione matrice')
st.sidebar.write('Scrivere la matrice quadrata come da esempio Matrice: 1,2;4,5')
st.sidebar.write('Usare la , per separe le varie colonne e il ; per andare alla prossima riga')
input_matrice=st.sidebar.text_area('Scrivere Matrice:')

# Creazione matrice
matrice = np.matrix(input_matrice)
matrice_array = np.asarray(matrice)

##### Creazione Due colonne per output ##############################################################
left_column1, right_column1 = st.beta_columns(2)
left_column2, right_column2 = st.beta_columns(2)

## Visualizzazione matrice
with left_column1:
    st.header('Matrice Quadrata Creata:')
    matrice_array
with right_column1: 
    st.header('Visualizzazione del grafo:')
    
##### Creaizone Input per calcolo #######################################################
st.sidebar.header('Calcolo percorso:')
st.sidebar.write('Calcolo del percorso più corto, Nx nodo di partenza e Ny nodo di arrivo. I nodi della matrice corrispondono agli indici della colonna.')
selezione = st.sidebar.radio("Seleziona tipo di calcolo",('Da Nx a tutti più vicini','Da Nx a Ny'))
if selezione == 'Da Nx a tutti più vicini':
    nodo_partenza=np.int(st.sidebar.number_input('Scrivere nodo di partenza (Numero intero):'))
    bottone_calcolo = st.sidebar.button('Calcola percorso', key=1)
    if bottone_calcolo:
        grafo_matrice = nx.from_numpy_matrix(matrice_array)
        percorso = nx.single_source_dijkstra_path(grafo_matrice, nodo_partenza, weight='weight')
        lunghezza = nx.single_source_dijkstra_path_length(grafo_matrice, nodo_partenza, weight='weight')
        with left_column2:
            st.header('Percorsi:')
            st.write('Qui vengono mostrati i vari percorsi che sono stati trovati. I valori a destra corrispondono al ordine di successione, mentre I valori a destra i vari nodi.') 
            percorso
        with right_column2:
            st.header('Tempo percorso:')
            st.write('Qui viene mostrato il tempo totale del pecrorso più breve')
            lunghezza
        with right_column1:
            fig, ax = plt.subplots()
            ax = nx.draw(grafo_matrice, with_labels=True,node_color='skyblue',pos=nx.circular_layout(grafo_matrice))
            st.pyplot(fig)
elif selezione == 'Da Nx a Ny':
    nodo_partenza=np.int(st.sidebar.number_input('Scrivere nodo di partenza (Numero intero):'))
    nodo_arrivo=np.int(st.sidebar.number_input('Scrivere nodo di arrivo (Numero intero):'))
    bottone_calcolo = st.sidebar.button('Calcola percorso', key=2)
    if bottone_calcolo:
        grafo_matrice = nx.from_numpy_matrix(matrice_array)
        percorso = nx.shortest_path(grafo_matrice, source=nodo_partenza, target=nodo_arrivo, weight='weight')
        lunghezza = nx.shortest_path_length(grafo_matrice, source=nodo_partenza, target=nodo_arrivo, weight='weight')
        with left_column2:
            st.header('Percorso:')
            st.write('Qui viene mostrato il percorso trovato. I valori a destra corrispondono al ordine di successione, mentre I valori a destra i vari nodi.')
            percorso
        with right_column2:
            st.header('Tempi percorsi:')
            st.write('Qui vengono mostrati i vari tempi dei vari percorsi')
            lunghezza
        with right_column1:
            fig, ax = plt.subplots()
            ax = nx.draw(grafo_matrice, with_labels=True, node_color='skyblue',pos=nx.circular_layout(grafo_matrice))
            st.pyplot(fig) 
