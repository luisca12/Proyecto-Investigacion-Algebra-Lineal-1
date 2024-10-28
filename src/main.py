from src.utils import mkdir

import os

def main():
    while True:
        mkdir()
        from src.graphDef import graph
        from src.utils import checkIsDigit
        from src.log import sysLog
        from src.strings import greetingString, inputErrorString
        greetingString()
        nodeAmount = input(f"¿Cuántos nodos quiere agregar?: ")
        if checkIsDigit(nodeAmount) and int(nodeAmount) > 2:
            print('-'*50)
            graph(int(nodeAmount))
            break
        else:
            sysLog.error(f"Valor incorrecto: {nodeAmount}")
            inputErrorString()
            os.system("PAUSE")

if __name__ == "__main__":
    main()