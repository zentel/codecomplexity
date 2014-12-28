import os

def cyclomatic_complexity(edges, nodes, components):
    """Dada la cantidad de caminos posibles en el codigo (edges), la cantidad de nodos(nodes) y la cantidad de componentes - o binarios intervinientes - (components) calcula la complejidad ciclomatica, lo que demuestra cuan complejo es el flujo del codigo"""
    return edges - nodes + (2*components)

def halstead_complexity(operators, operands, total_operators, total_operands):
    """ Dada la cantidad de operadores y operandos unicos (sin repeticiones), y la cantidad total de operadores y operandos (con repeticiones) se realizan los diferentes calculos de Halstead para medir complejidad:
		Vocabulario: vocabulary = operators + operands
		Longitud: length = total_operators + total_operands
		Longitud calculada: calculated_length = operators*log(operators) + operands*log(operands)
		Volumen (describe el tamano de la implementacion de un algoritmo. Debe estar entre 20 y 1000 para una funcion/metodo): volume = length*log(vocabulary)
		Dificultad (nivel de dificultad para mantener, lo que lleva a mayor propension al error): difficulty = (operators/2)*(total_operands/operands)
		Esfuerzo (mide el esfuerzo de entender e implementar el codigo): effort = volume*difficulty """
    pass
	
def calcular_complejidad(function_count, output, path ="."):
    """ realiza el reporte de complejidad para todos los archivos en un path determinado, aplicando la funcion establecida para contabilizar, y escribiendo el reporte en output"""
     
    os.chdir(path)
    path_corregido = os.getcwd()
        
    archivos = os.listdir()
    for archivo in archivos:
        try:
            os.chdir(path_corregido + "\\" + archivo)
            print("Directorio: " + path_corregido + "\\" + archivo)
            calcular_complejidad(function_count, output, path_corregido + "\\" + archivo)
        except NotADirectoryError: 
            print("Archivo: " + archivo)
        else:
            print("Otro error")
    
class Contadores:
    """ Clase que debe utilizarse para ser devuelta por la funcion contabilizadora """
    edges = 0
    nodes = 0
    components = 0
    operators = 0
    operands = 0
    total_operators = 0
    total_operands = 0
    
if __name__ == "__main__":
    import sys