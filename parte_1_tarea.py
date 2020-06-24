#####CREAR GRAFO######
#import networkx as nx
#G = nx.DiGraph()

######  NODOS  #######
#G.add_node()

######  ARCOS  #######
#(2, 3, {'weight': 3.1415})
#escribir arcos asi
#G.add_edge()
import time
import networkx as nx
def crear_grafo_distancia(distancias):
    grafo_distancias = nx.DiGraph()
    with open("distancias.txt") as distancias:
        lineas = distancias.readlines()      #lista cada elemento es una linea del archivo
        for linea in lineas:              #para ver cada linea
            linea=linea.strip("\n")       #le sacamos el \n
            linea=linea.split(" ")        #hacemos listas de cada string
            grafo_distancias.add_node(linea[1])         #si se repiten, no se vuelve a escribir, es como un set
            grafo_distancias.add_node(linea[2])
            grafo_distancias.add_edge(linea[1] , linea[2], {'distancia' : linea[3]})    # aca cada arco con su distancia
    return grafo_distancias


def crear_grafo_tiempo(tiempos):
    grafo_tiempos = nx.DiGraph()
    with open("tiempos.txt") as tiempos:
        lineas = tiempos.readlines()      #lista cada elemento es una linea del archivo
        for linea in lineas:              #para ver cada linea
            linea=linea.strip("\n")       #le sacamos el \n
            linea=linea.split(" ")        #hacemos listas de cada string
            grafo_tiempos.add_node(linea[2])
            grafo_tiempos.add_edge(linea[1] , linea[2], {'tiempo' : int(linea[3])})    # aca cada arco con su tiempo
    return grafo_tiempos

def origenes(origenes):
    with open("origenes.txt") as origenes:
        lineas=origenes.readlines()      #esto me deberia dar una lista con una lista adentro, que tiene como elementos a los origenes
        for linea in lineas:             #para acceder a la lista de adentro
            return linea                 # Me entrega la lista con todos los origenes

def destinos(destinos):
    with open("destinos.txt") as destinos:
        lineas=destinos.readlines()     #lo mismo que la funcion anterior pero para los destinos
        for linea in lineas:
            return linea

orig = origenes("origenes.txt")
dest = destinos("destinos.txt")
grafo_tiempos = crear_grafo_distancia("distancias.txt")
grafo_distancias = crear_grafo_tiempo("tiempos.txt")

for origen in orig:
    for destino in destinos:     #esto es como una doble sumatoria (sum en origenes y despues sum en destinos)
        #Ahora todo lo de Bellman-Ford
        tiempo_1_bf = time.time()
        ruta_distancias = nx.bellman_ford_path(grafo_distancias, origen, destino, weight = 'distancia')
        tiempo_2_bf = time.time()
        largo_ruta = len(ruta_distancias)
        distancia_total = 0
        for i in range (largo_ruta - 1):
            diccionario = grafo_distancias.get_edge_data(ruta_distancias[i], ruta_distancias[i+1]) # me da un diccionario {distancia: x}
            distancia_total += diccionario['distancia']
        print('BELLMAN-FORD \nOrígen:', origen, 'Destino:', destino , '\nRuta mínima según las distancias:', ruta_distancias, '\ndistancia:', distancia_total, '\ntiempo de ejecución:', tiempo_2_bf - tiempo_1_bf)

        tiempo_3_bf = time.time()
        ruta_tiempos = nx.bellman_ford_path(grafo_tiempos, origen, destino, weight = 'tiempo')
        tiempo_4_bf = time.time()
        largo_ruta_t = len(ruta_tiempos)
        tiempo_total = 0
        for i in range (largo_ruta_t - 1):
            diccionario_t = grafo_tiempos.get_edge_data(ruta_tiempos[i], ruta_tiempos[i+1]) # me da un diccionario {distancia: x}
            tiempo_total += diccionario_t['tiempo']
        print('BELLMAN-FORD \nOrígen:', origen, 'Destino:', destino , '\nRuta mínima según los tiempos:', ruta_tiempos, ' \ntiempo:', tiempo_total, '\ntiempo de ejecución:', tiempo_3_bf - tiempo_4_bf)
        #Ahora Dijkstra
        tiempo_1_dijkstra = time.time()
        ruta_distancias_dijkstra = nx.dijkstra_path(grafo_distancias, origen, destino, weight = 'distancia')
        tiempo_2_dijkstra = time.time()
        largo_ruta_dijkstra = len(ruta_distancias_dijkstra)
        distancia_total_dijkstra = 0
        for i in range (largo_ruta_dijkstra - 1):
            diccionario_dijkstra = grafo_distancias.get_edge_data(ruta_distancias_dijkstra[i], ruta_distancias_dijkstra[i+1]) 
            distancia_total_dijkstra += diccionario_dijkstra['distancia']
        print('DIJKSTRA \nOrígen:', origen, 'Destino:', destino , '\nRuta mínima según las distancias:', ruta_distancias_dijkstra, '\ndistancia:', distancia_total_dijkstra, '\ntiempo de ejecución:', tiempo_2_dijkstra - tiempo_1_dijkstra)

        tiempo_3_dijkstra = time.time()
        ruta_tiempos_dijkstra = nx.dijkstra_path(grafo_tiempos, origen, destino, weight = 'tiempo')
        tiempo_4_dijkstra = time.time()
        largo_ruta_t_dijkstra = len(ruta_tiempos_dijkstra)
        tiempo_total_dijkstra = 0
        for i in range (largo_ruta_t_dijkstra - 1):
            diccionario_t_dijkstra = grafo_tiempos.get_edge_data(ruta_tiempos_dijkstra[i], ruta_tiempos_dijkstra[i+1])
            tiempo_total_dijkstra += diccionario_t_dijkstra['tiempo']
        print('DIJKSTRA \nOrígen:', origen, 'Destino:', destino , '\nRuta mínima según los tiempos:', ruta_tiempos_dijkstra, ' \ntiempo:', tiempo_total_dijkstra, '\ntiempo de ejecución:', tiempo_3_dijkstra - tiempo_4_dijkstra)
        #Ahora Dijkstra Bidireccional
        tiempo_1_bidijkstra=time.time()
        length,path = nx.bidirectional_dijkstra(grafo_distancias, origen, destino, weight = 'distancia')
        ruta_distancias_bidijkstra = bidirectional_dijkstra(grafo_distancias, origen, destino, weight = 'distancia')
        tiempo_2_bidijkstra=time.time()
        print('DIJKSTRA BIDIRECCIONAL \nOrígen:', origen, 'Destino:', destino ,'\nRuta mínima según las distancias:', path, '\ndistancia:', length, '\ntiempo de ejecución:', tiempo_2_bidijkstra - tiempo_1_bidijkstra)

        tiempo_3_bidijkstra = time.time()
        length,path = nx.bidirectional_dijkstra(grafo_tiempos, origen, destino, weight = 'tiempo')
        tiempo_4_bidijkstra = time.time()
        print('DIJKSTRA BIDIRECCIONAL \nOrígen:', origen, 'Destino:', destino ,'\nRuta mínima según los tiempos:', path, ' \ntiempo:', length, '\ntiempo de ejecución:', tiempo_3_dijkstra - tiempo_4_dijkstra)
        






########################################### 
########  PARA HACER BELLMAN-FORD  ########
###########################################
### bellman_ford_path(G, source, target, weight='weight') el weight es 'distancia' o 'tiempo'
###########################################
#https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.bellman_ford_path.html#networkx.algorithms.shortest_paths.weighted.bellman_ford_path

###########################################
#########   PARA HACER DIJKSTRA   #########
###########################################
##### dijkstra_path(G, source, target, weight='weight')
###########################################
#https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.dijkstra_path.html#networkx.algorithms.shortest_paths.weighted.dijkstra_path

###########################################
#### PARA HACER DIJKSTRA BIDIRECCIONAL ####
###########################################
#bidirectional_dijkstra(G, source, target, weight='weight')
###########################################
#https://networkx.github.io/documentation/networkx-1.8/reference/generated/networkx.algorithms.shortest_paths.weighted.bidirectional_dijkstra.html

###########################################
############## PARA HACER A* ##############
###########################################
#astar_path(G, source, target, heuristic=None, weight='weight')
###########################################
#https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.astar.astar_path.html#networkx.algorithms.shortest_paths.astar.astar_path