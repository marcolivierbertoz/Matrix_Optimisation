# Loading packages ##########################################################################
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

###############################################################################################
st.set_page_config(layout="wide")

##### Creazione expander per matrice ########################################################
with st.beta_expander('Creazione Matrice', expanded=True):
    st.write('Scrivere la matrice quadrata come da esempio Matrice: 1,2;4,5')
    st.write('Usare la , per separe le varie colonne e il ; per andare alla prossima riga')
    input_matrice=st.text_area('Scrivere Matrice:')

# Creazione matrice
matrice = np.matrix(input_matrice)
matrice_array = np.asarray(matrice)

# Creazione grafo

##### Creazione Due colonne per output ##############################################################
left_column1, right_column1 = st.beta_columns(2)
left_column2, right_column2 = st.beta_columns(2)

## Visualizzazione matrice
with left_column1:
    st.header('Matrice Quadrata Creata:')
    matrice_array
with right_column1: 
    st.header('Visualizzazione del grafo:')

## Define fucntion for creating a list of numbers
@st.cache
def lista_numeri(inizio,fine):
    return np.arange(inizio,fine,1)
    
##### Creaizone Input per calcolo #######################################################
st.sidebar.header('Calcolo percorso:')
st.sidebar.write('Calcolo del percorso più corto, Nx nodo di partenza e Ny nodo di arrivo. I nodi della matrice corrispondono agli indici della colonna.')
selezione = st.sidebar.radio("Seleziona tipo di calcolo",('Da Nx a tutti più vicini','Da Nx a Ny'))
if selezione == 'Da Nx a tutti più vicini':
    nodo_partenza=np.int(st.sidebar.number_input('Scrivere nodo di partenza (Numero intero):'))
    bottone_calcolo = st.sidebar.button('Calcola percorso', key=1)
    if bottone_calcolo:
        grafo_matrice = nx.from_numpy_matrix(matrice_array, create_using=nx.Graph)
        percorso = nx.single_source_dijkstra_path(grafo_matrice, nodo_partenza, weight='weight')
        lunghezza = nx.single_source_dijkstra_path_length(grafo_matrice, nodo_partenza, weight='weight')
        indici_lista = lista_numeri(0,len(percorso))
        # selezione_percorso = st.sidebar.selectbox('Seleziona percorso', indici_lista)
        with left_column2:
            st.header('Percorsi:')
            st.write('Visione dei vari percorsi trovati con i relativi nodi:') 
            percorso
        with right_column2:    
            st.header('Tempi percorsi:')
            st.write('Visione dei vari tempi totali dei vari percorsi')
            lunghezza
        with right_column1:
            fig1, ax1 = plt.subplots()
            G1=grafo_matrice
            layout= nx.circular_layout(G1)
            labels = nx.get_edge_attributes(G1, 'weight')
            ax1 = nx.draw(G1, with_labels=True,node_color='skyblue',pos=layout)
            st.pyplot(fig1)
elif selezione == 'Da Nx a Ny':
    nodo_partenza=np.int(st.sidebar.number_input('Scrivere nodo di partenza (Numero intero):'))
    nodo_arrivo=np.int(st.sidebar.number_input('Scrivere nodo di arrivo (Numero intero):'))
    st.sidebar.header('Opzioni grafico:')
    mostrare_tempi=st.sidebar.radio("Vuoi mostrare i tempi di collegamento dei grafi:",('Si','No'))
    bottone_calcolo = st.sidebar.button('Calcola percorso', key=2)
    if bottone_calcolo:
        grafo_matrice = nx.from_numpy_matrix(matrice_array, create_using=nx.Graph)
        percorso = nx.dijkstra_path(grafo_matrice, source=nodo_partenza, target=nodo_arrivo, weight='weight')
        lunghezza = nx.dijkstra_path_length(grafo_matrice, source=nodo_partenza, target=nodo_arrivo, weight='weight')
        with left_column2:
            st.header('Percorso:')
            st.write('Qui viene mostrato il percorso trovato. I valori a sinistra corrispondono al ordine di successione, mentre I valori a destra i vari nodi.')
            percorso
            st.header('Tempo percorso:')
            st.write('Qui viene mostrato il tempo totale del percorso più breve')
            lunghezza
        with right_column1:
            fig1, ax1 = plt.subplots()
            G1=grafo_matrice
            layout= nx.circular_layout(G1)
            labels = nx.get_edge_attributes(G1, 'weight')
            ax1 = nx.draw(G1, with_labels=True,node_color='skyblue',pos=layout)
            st.pyplot(fig1)
        with right_column2:
            if mostrare_tempi == 'Si':
                st.header('Grafico del percorso:')
                fig2, ax2 = plt.subplots()
                G2 = grafo_matrice
                layout= nx.circular_layout(G2)
                labels = nx.get_edge_attributes(G2, 'weight')
                ax2 = nx.draw(G2, with_labels=True,node_color='w',pos=layout, edge_color='w')
                # ax2 = nx.draw_networkx_edges(G2,pos=layout, edge_color='w')
                # Disegno del percorso
                path_edges = zip(percorso,percorso[1:])
                path_edges = set(path_edges)
                ax2 = nx.draw_networkx_nodes(G2, pos=layout,nodelist=percorso,node_color='r')
                ax2 = nx.draw_networkx_edges(G2, pos=layout, edgelist=path_edges,edge_color='r')
                ax2 = nx.draw_networkx_edge_labels(G2, pos=layout, edge_labels=labels, alpha=1,font_size=5)
                st.pyplot(fig2)
            elif mostrare_tempi == 'No':
                st.header('Grafico del percorso:')
                fig2, ax2 = plt.subplots()
                G2 = grafo_matrice
                layout= nx.circular_layout(G2)
                labels = nx.get_edge_attributes(G2, 'weight')
                ax2 = nx.draw(G2, with_labels=True,node_color='w',pos=layout, edge_color='w')
                # ax2 = nx.draw_networkx_edges(G2,pos=layout, edge_color='w')
                # Disegno del percorso
                path_edges = zip(percorso,percorso[1:])
                path_edges = set(path_edges)
                ax2 = nx.draw_networkx_nodes(G2, pos=layout,nodelist=percorso,node_color='r')
                ax2 = nx.draw_networkx_edges(G2, pos=layout, edgelist=path_edges,edge_color='r')
                # ax2 = nx.draw_networkx_edge_labels(G2, pos=layout, edge_labels=labels, alpha=0.5,font_size=5)
                st.pyplot(fig2)

