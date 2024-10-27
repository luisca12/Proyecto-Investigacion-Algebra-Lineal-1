import os

def greetingString():
        os.system("CLS")
        print('  ------------------------------------------------------ ')
        print(f"      Bienvenido al programa para visualizar una red")
        print(f"        y calcular el camino mas corto usando: ")
        print(f"            NetworkX, Dijkstra y Matplotlib")
        print('  ------------------------------------------------------ ')

def inputErrorString():
        os.system("CLS")
        print('  ------------------------------------------------------------ ')  
        print('>      INPUT ERROR: Solo se aceptan numeros mayores a 1       <')
        print('  ------------------------------------------------------------ ')
