import os
import sys

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
    coleccion_contadores = []
    archivos = os.listdir()
    
    for archivo in archivos:
        if os.path.isdir(path_corregido + "\\" + archivo): #es un directorio, recorrerlo
            print("Directorio: " + path_corregido + "\\" + archivo)
            os.chdir(path_corregido + "\\" + archivo)
            coleccion_contadores.extend(calcular_complejidad_int(function_count, path_corregido + "\\" + archivo))
        elif os.path.isfile(path_corregido + "\\" + archivo): #es un archivo, procesarlo
            coleccion_contadores.append(function_count(path_corregido + "\\" + archivo))
        else:
            print("Ouch! no es un archivo")
            
    for c in coleccion_contadores:
        print("{0:60}|{1:3d}|{2:3d}|{3:3d}|{4:3d}|{5:3d}|{6:3d}|{7:3d}|{8:3d}".format(c.archivo,c.lines, c.edges, c.nodes, c.components, c.operators, c.operands, c.total_operators, c.total_operands))
    
    print ("{0:4d} archivos procesados".format(len(archivos)))   # TODO: ARREGLAR!!!!
        

def calcular_complejidad_int(function_count, path):
    """ Función interna, para aplicar recursividad entre los directorios donde se encuentren los fuentes"""
    os.chdir(path)
    path_corregido = os.getcwd()
    coleccion_contadores = []
    archivos = os.listdir()
    
    for archivo in archivos:
        if os.path.isdir(path_corregido + "\\" + archivo): #es un directorio, entonces hay que recorrerlo
            print("Directorio: " + path_corregido + "\\" + archivo)
            os.chdir(path_corregido + "\\" + archivo)            
            coleccion_contadores.extend(calcular_complejidad_int(function_count, path_corregido + "\\" + archivo))
        elif os.path.isfile(path_corregido + "\\" + archivo):  #es un archivo, procesarlo
            coleccion_contadores.append(function_count(path_corregido + "\\" + archivo))
        else:
            print("Ouch! " + repr(sys.exc_info()[0]))
    
    return coleccion_contadores
    
    
class Contadores:
    """ Clase que debe utilizarse para ser devuelta por la funcion contabilizadora """
    archivo = ""
    lines = 0
    edges = 0
    nodes = 0
    components = 0
    operators = 0
    operands = 0
    total_operators = 0
    total_operands = 0
    
if __name__ == "__main__":
    import sys