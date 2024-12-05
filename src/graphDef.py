from utils import exportGraphtoCSV
from log import sysLog

import networkx as nx
import matplotlib.pyplot as plt
import traceback
import random

def graph(nodeAmount):
    """
    This function creates a graph using NetworkX and determines the best path using Dijkstra

    **Args:**
        nodeAmount: Int, it receives any specified amount of nodes
        
    **Returns:**
        None
    """
    try:
        # Agregar nodos y aristas con pesos manualmente
        # G.add_edge('Nodo1', 'Nodo2', weight=4)
        # G.add_edge('Nodo2', 'Nodo3', weight=6)
        # G.add_edge('Nodo1', 'Nodo3', weight=10)
        # G.add_edge('Nodo3', 'Nodo4', weight=3)
        # G.add_edge('Nodo2', 'Nodo4', weight=7)

        # Definición de Variables
        paths = {}
        nodeAmountInt = int(nodeAmount)

        # Se crea un grafo en blanco
        graph = nx.Graph()

        # Conecta nodos consecutivos con aristas de pesos aleatorios
        for i in range(1, nodeAmountInt):
            print(i)
            graph.add_edge(f'Nodo {i}', f'Nodo {i+1}', weight=random.randint(1, 20))
            print(f"Added Node {i} and Node Node {i + 1}")

        # Conecta cada nodo con un número aleatorio de enlaces a otros nodos, asegurándose de que no haya enlaces a sí mismo
        for i in range(1, nodeAmountInt):
            numLinksForNode = random.randint(1, nodeAmountInt)
            linksAdded = 0
            while linksAdded < numLinksForNode:
                nodeY = random.randint(1, nodeAmountInt)

                if nodeY != i:
                    weight = random.randint(1, 20)
                    graph.add_edge(f'Nodo {i}', f'Nodo {nodeY}', weight=weight)
                    linksAdded += 1
                    print(f"Link added: Nodo {i} to Nodo {nodeY} with weight {weight}")

        # Imprime información sobre las aristas con sus pesos
        print("Aristas del grafo con pesos:")
        for u, v, weight in graph.edges(data=True):
            print(f"{u} -- {v}, peso: {weight['weight']}")

        # Usado para retornar los nodos de un grafo
        nodeList = list(graph.nodes)

        # Pregunta al usuario donde quiere que inicie el camino.
        srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()
        while srcNode not in nodeList:
            print("Nodo no válido. Por favor, elige un nodo de la lista.")
            srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()

        # Pregunta al usuario donde quiere que termine el camino.
        dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()
        while dstNode not in nodeList or dstNode == srcNode:
            if dstNode == srcNode:
                print("El nodo de destino no puede ser el mismo que el nodo de inicio.")
            else:
                print("Nodo no válido. Por favor, elige un nodo de la lista.")
            dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()

        # Aqui itera sobre todos los posibles caminos de un Punto A al B
        for path in nx.all_simple_paths(graph, source=srcNode, target=dstNode):
            # Calcula la longitud del camino sumando los pesos de las aristas
            lengthOut = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            # Almacena la longitud en un diccionario: [(#,#)]
            paths[tuple(path)] = lengthOut

        # Extrae las longitudes de todos los caminos en una lista 
        pathsLengths = list(paths.values())

        # Encuentra la longitud mínima de todos los caminos
        minLenght = min(pathsLengths)
        # Encuentra la longitud máxima de todos los caminos
        maxLenght = max(pathsLengths)

        # Asigna el color verde la mejor camino, rojo al peor y amarillo al resto
        colors = ['green' if length == minLenght else 'red' if length == maxLenght else 'yellow' for length in pathsLengths]

        # Crea una nueva figura para los gráficos de Matplotlib con un tamaño de 10x6 pulgadas
        allPathsFigure = plt.figure(figsize=(10, 6)).add_subplot(111)

        # Crea una lista para clasificar el mejor, peor y posibles caminos
        handles = [
            plt.Line2D([0], [0], color='green', lw=4, label='Mejor camino'),
            plt.Line2D([0], [0], color='red', lw=4, label='Peor Camino'),
            plt.Line2D([0], [0], color='yellow', lw=4, label='Posibles Caminos')
        ]

        # Crea una leyenda
        allPathsFigure.legend(handles=handles, loc='upper right', fontsize=10)

        # Se obtiene el administrador de la figura actual (para poder modificar propiedades de la ventana del gráfico)
        windowTittle = plt.get_current_fig_manager()
        # Se define el título de la ventana del gráfico con el formato especificado, incluyendo los nodos de origen y destino
        windowTittle.set_window_title(f"Todos los caminos de {srcNode} a {dstNode}")

        # Crea un gráfico de barras horizontal
        bars = allPathsFigure.barh(range(len(pathsLengths)), pathsLengths, tick_label=[str(path) for path in paths.keys()],height=0.4, color=colors, alpha=0.8)
        allPathsFigure.set_title(f'Peso de todos los caminos de {srcNode} a {dstNode}', fontsize=16, fontweight='bold')
        
        # Etiqueta para el eje X
        allPathsFigure.set_xlabel('Peso', fontsize=12)
        
        # Etiqueta para el eje Y
        allPathsFigure.set_ylabel('Caminos', fontsize=12)

        # Activa la cuadrícula en el eje X con un estilo de línea punteada y transparencia
        allPathsFigure.grid(axis='x', linestyle='--', alpha=0.7)

        # Itera sobre cada barra horizontal, agrega estilo y el peso al final de cada barra
        for bar in bars:
            allPathsFigure.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                                f'{bar.get_width()}', 
                                va='center', ha='left', fontsize=7, fontweight='bold', color='black')
        # Ajusta el diseño del gráfico para que todo encaje bien dentro del área disponible
        plt.tight_layout()
        # Exporta los datos del gráfico a un archivo CSV
        exportGraphtoCSV(graph, srcNode, dstNode)
        # Muestra el gráfico de manera no bloqueante, permitiendo que la ejecución del código continúe
        plt.show(block=False)
        
        # Calcula el camino más corto usando Dijkstra
        bestPath = nx.dijkstra_path(graph, source=srcNode, target=dstNode, weight='weight')
        print(f"\nEl camino más corto de {srcNode} a {dstNode} es: {bestPath}")

        # Calcula la longitud del camino más corto
        bestLength = nx.dijkstra_path_length(graph, source=srcNode, target=dstNode, weight='weight')
        print(f"La longitud total del camino más corto es: {bestLength}")

        # Calcula las posiciones de los nodos para el diseño del grafo utilizando el algoritmo de disposición por resorte
        pos = nx.spring_layout(graph) 

        # Crea una nueva figura para graficar el mejor camino
        bestPathFigure = plt.figure(figsize=(10, 6)).add_subplot(111)

        # Obtiene el administrador de la figura actual y establece el título de la ventana con el mejor camino entre los nodos
        windowTittle = plt.get_current_fig_manager()
        windowTittle.set_window_title(f"Mejor camino de {srcNode} a {dstNode}")

        # Dibuja el grafo en la figura utilizando las posiciones calculadas
        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

        # Obtiene los pesos de las aristas y los dibuja como etiquetas sobre las aristas del grafo
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        # Crea una lista de las aristas del mejor camino
        path_edges = list(zip(bestPath, bestPath[1:])) 

        # Dibuja las aristas del mejor camino en rojo, ancho 2.5
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2.5)

        # Establece el título de la figura que muestra el grafo y el mejor camino
        bestPathFigure.set_title("Visualización del Grafo y Camino Más Corto", fontsize=16, fontweight='bold')
        plt.show()

    except nx.NetworkXNoPath:
        print(f"No hay ruta disponible entre {srcNode} y {dstNode}")

    except Exception as error:
        print(f"ERROR: An error occurred: {error}\n", traceback.format_exc())
        sysLog.error(traceback.format_exc())