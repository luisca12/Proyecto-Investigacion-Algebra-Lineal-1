# Importar las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt

# 1. Construcción de grafos con NetworkX
# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos y aristas con pesos
G.add_edge('Nodo1', 'Nodo2', weight=4)
G.add_edge('Nodo2', 'Nodo3', weight=6)
G.add_edge('Nodo1', 'Nodo3', weight=10)
G.add_edge('Nodo3', 'Nodo4', weight=3)
G.add_edge('Nodo2', 'Nodo4', weight=7)

# Mostrar las aristas con sus pesos
print("Aristas del grafo con pesos:")
for u, v, weight in G.edges(data=True):
    print(f"{u} -- {v}, peso: {weight['weight']}")

# 2. Implementación del Algoritmo de Dijkstra
# Calcular el camino más corto desde 'Nodo1' a 'Nodo4' utilizando el algoritmo de Dijkstra
path = nx.dijkstra_path(G, source='Nodo1', target='Nodo4', weight='weight')
print(f"\nEl camino más corto de Nodo1 a Nodo4 es: {path}")

# Obtener la longitud (peso total) del camino más corto
length = nx.dijkstra_path_length(G, source='Nodo1', target='Nodo4', weight='weight')
print(f"La longitud total del camino más corto es: {length}")

# 3. Análisis de resultados
# Comprobar si el algoritmo selecciona el camino más corto
# Aquí podrías agregar pruebas con diferentes configuraciones de grafos y comparar los resultados

# 4. Visualización de grafos
# Dibujar el grafo
pos = nx.spring_layout(G)  # Posiciones de los nodos para la visualización
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)

# Dibujar las etiquetas de los pesos en las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Resaltar el camino más corto en el grafo visualizado
path_edges = list(zip(path, path[1:]))  # Crear una lista de aristas en el camino más corto
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)

# Mostrar el grafo
plt.title("Visualización del Grafo y Camino Más Corto")
plt.show()
