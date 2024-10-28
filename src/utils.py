import traceback
import networkx as nx
import csv
import os
import logging.config
import traceback

infoLog = logging.getLogger('infoLog')

def mkdir():
    path = "logs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            print(traceback.format_exc())

def exportGraphtoCSV(graph, srcNode, dstNode, filename='Todos los posibles caminos.csv'):
    """
    Export all simple paths from srcNode to dstNode in the graph to a CSV file.

    **Args:**
        graph: The NetworkX graph containing the paths.
        srcNode: The starting node.
        dstNode: The ending node.
        filename: The name of the CSV file to create.
        
    **Returns:**
        None
    """
    paths = {}

    with open(filename, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        if csvFile.tell() == 0:
            writer.writerow(['Path', 'Weight', 'Notes'])

        for path in nx.all_simple_paths(graph, source=srcNode, target=dstNode):
            lengthOut = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            paths[tuple(path)] = lengthOut
            
        bestPath = min(paths.values())
        worstPath = max(paths.values())

        for path, lengthOut in paths.items():
            if lengthOut == bestPath:
                writer.writerow([' -> '.join(path), lengthOut, 'Best Path'])
            elif lengthOut == worstPath:
                writer.writerow([' -> '.join(path), lengthOut, 'Worst Path'])
            else:
                writer.writerow([' -> '.join(path), lengthOut])

    print(f"Grafo exportado como: {filename}")

def checkIsDigit(input_str):
    """
    This function checks if the provided string is a digit.

    **Args:**
        input_str: The string to be checked.
        
    **Returns:**
        bool: True if the string is a digit, False otherwise.
    """
    try:
        input_str = input_str.strip()
        infoLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.isdigit()
    
    except Exception as error:
        infoLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        infoLog.error(traceback.format_exc())