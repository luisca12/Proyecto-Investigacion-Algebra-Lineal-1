from src.functions import checkIsDigit
from src.log import sysLog

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import time
import traceback
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
    try:
        paths = {}

        nodeAmountInt = int(nodeAmount)
        graph = nx.Graph()

        for i in range(1, nodeAmountInt):
            print(i)
            graph.add_edge(f'Nodo {i}', f'Nodo {i+1}', weight=random.randint(1, 20))

        numLinks = random.randint(1, nodeAmountInt * 2)  # Número de aristas entre nodos
        linksAdded = 0
        while linksAdded < numLinks:
            nodeX = random.randint(1, nodeAmountInt)
            nodeY = random.randint(1, nodeAmountInt)

            if nodeX != nodeY:
                weight = random.randint(1, 20)
                graph.add_edge(f'Nodo {nodeX}', f'Nodo {nodeY}', weight=weight)
                
                linksAdded += 1
                print(f"Links added: {linksAdded}")

        print("Aristas del grafo con pesos:")
        for u, v, weight in graph.edges(data=True):
            print(f"{u} -- {v}, peso: {weight['weight']}")

        nodeList = list(graph.nodes)

        srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()
        while srcNode not in nodeList:
            print("Nodo no válido. Por favor, elige un nodo de la lista.")
            srcNode = input(f"¿Dónde quiere que inicie el camino? (Opciones: {', '.join(nodeList)}): ").strip()

        dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()
        while dstNode not in nodeList or dstNode == srcNode:
            if dstNode == srcNode:
                print("El nodo de destino no puede ser el mismo que el nodo de inicio.")
            else:
                print("Nodo no válido. Por favor, elige un nodo de la lista.")
            dstNode = input(f"¿Dónde quiere que termine el camino? (Opciones: {', '.join(nodeList)}): ").strip()

        for path in nx.all_simple_paths(graph, source=srcNode, target=dstNode):
            lengthOut = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            paths[tuple(path)] = lengthOut

        pathsLengths = list(paths.values())

        minLenght = min(pathsLengths)
        maxLenght = max(pathsLengths)

        colors = ['green' if length == minLenght else 'red' if length == maxLenght else 'yellow' for length in pathsLengths]

        allPathsFigure = plt.figure(figsize=(10, 6)).add_subplot(111)

        handles = [
            plt.Line2D([0], [0], color='green', lw=4, label='Mejor camino'),
            plt.Line2D([0], [0], color='red', lw=4, label='Peor Camino'),
            plt.Line2D([0], [0], color='yellow', lw=4, label='Posibles Caminos')
        ]

        allPathsFigure.legend(handles=handles, loc='upper right', fontsize=10)

        windowTittle = plt.get_current_fig_manager()
        windowTittle.set_window_title(f"Todos los caminos de {srcNode} a {dstNode}")

        bars = allPathsFigure.barh(range(len(pathsLengths)), pathsLengths, tick_label=[str(path) for path in paths.keys()],height=0.4, color=colors, alpha=0.8)
        allPathsFigure.set_title(f'Peso de todos los caminos de {srcNode} a {dstNode}', fontsize=16, fontweight='bold')
        allPathsFigure.set_xlabel('Peso', fontsize=12)
        allPathsFigure.set_ylabel('Caminos', fontsize=12)
        allPathsFigure.grid(axis='x', linestyle='--', alpha=0.7)

        for bar in bars:
            allPathsFigure.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                                f'{bar.get_width()}', 
                                va='center', ha='left', fontsize=7, fontweight='bold', color='black')
        plt.tight_layout()
        plt.show(block=False)
        
        bestPath = nx.dijkstra_path(graph, source=srcNode, target=dstNode, weight='weight')
        print(f"\nEl camino más corto de {srcNode} a {dstNode} es: {bestPath}")

       
        bestLength = nx.dijkstra_path_length(graph, source=srcNode, target=dstNode, weight='weight')
        print(f"La longitud total del camino más corto es: {bestLength}")

        pos = nx.spring_layout(graph) 
        bestPathFigure = plt.figure(figsize=(10, 6)).add_subplot(111)
        windowTittle = plt.get_current_fig_manager()
        windowTittle.set_window_title(f"Mejor camino de {srcNode} a {dstNode}")
        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

        path_edges = list(zip(bestPath, bestPath[1:])) 
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2.5)
        
        bestPathFigure.set_title("Visualización del Grafo y Camino Más Corto", fontsize=16, fontweight='bold')
        plt.show()

    except nx.NetworkXNoPath:
        print(f"No hay ruta disponible entre {srcNode} y {dstNode}")

    except Exception as error:
        print(f"ERROR: An error occurred: {error}\n", traceback.format_exc())
        sysLog.error(traceback.format_exc())