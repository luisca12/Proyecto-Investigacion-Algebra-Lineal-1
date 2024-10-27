from src.functions import checkIsDigit

# Importar las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt
import random
import os

def graph(nodeAmount):
    """
    This function creates a graph using NetworkX and determines the best path using Dijkstra

    **Args:**
        nodeAmount: Int, it receives any specified amount of nodes
        
    **Returns:**
        None
    """
    
    nodeAmountInt = int(nodeAmount)
    edgeList = []
    for i in range(1, nodeAmountInt + 1):
        for j in range(1, nodeAmountInt + 1):
            if i != j:
                edgeList.append((f'Nodo{i}', f'Nodo{j}'))
    # 1. Construcción de grafos con NetworkX
    # Crear un grafo vacío
    graph = nx.Graph()
    # Agregar nodos y aristas con pesos
    for x, y in edgeList:
        weight = random.randint(1, 20)  # Peso aleatorio entre 1 y 20
        graph.add_edge(x, y, weight=weight)

    # Mostrar las aristas con sus pesos
    print("Aristas del grafo con pesos:")
    for u, v, weight in graph.edges(data=True):
        print(f"{u} -- {v}, peso: {weight['weight']}")

    nodeList = list(graph.nodes)
    srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()

    while srcNode not in nodeList:
        print("Nodo no válido. Por favor, elige un nodo de la lista.")
        srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()

    dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()

    # Validar que el nodo de destino ingresado sea válido y que no sea el mismo que srcNode
    while dstNode not in nodeList or dstNode == srcNode:
        if dstNode == srcNode:
            print("El nodo de destino no puede ser el mismo que el nodo de inicio.")
        else:
            print("Nodo no válido. Por favor, elige un nodo de la lista.")
    
        dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()

    # 2. Implementación del Algoritmo de Dijkstra
    # Calcular el camino más corto desde 'Nodo1' a 'Nodo4' utilizando el algoritmo de Dijkstra
    path = nx.dijkstra_path(graph, source=srcNode, target=dstNode, weight='weight')
    print(f"\nEl camino más corto de {srcNode} a {dstNode} es: {path}")

    # Obtener la longitud (peso total) del camino más corto
    length = nx.dijkstra_path_length(graph, source=srcNode, target=dstNode, weight='weight')
    print(f"La longitud total del camino más corto es: {length}")

    # 3. Análisis de resultados
    # Comprobar si el algoritmo selecciona el camino más corto
    # Aquí podrías agregar pruebas con diferentes configuraciones de grafos y comparar los resultados

    # 4. Visualización de grafos
    # Dibujar el grafo
    pos = nx.spring_layout(graph)  # Posiciones de los nodos para la visualización
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

    # Dibujar las etiquetas de los pesos en las aristas
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Resaltar el camino más corto en el grafo visualizado
    path_edges = list(zip(path, path[1:]))  # Crear una lista de aristas en el camino más corto
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2.5)

    # Mostrar el grafo
    plt.title("Visualización del Grafo y Camino Más Corto")
    plt.show()
