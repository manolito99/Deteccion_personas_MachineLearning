from deteccion import humanDetector
from deteccion import argsParser

if __name__ == "__main__":
    args = argsParser()
    print('Cargando...')
    Iniciar = humanDetector(args)
    print('Proceso Finalizado')
    
    