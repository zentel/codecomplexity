import os
import sys
import math

def cyclomatic_complexity(edges, nodes, components):
    """Dada la cantidad de caminos posibles en el codigo (edges), la cantidad de nodos(nodes) y la cantidad de componentes - o binarios intervinientes - (components) calcula la complejidad ciclomatica, lo que demuestra cuan complejo es el flujo del codigo"""
    return edges - nodes + (2*components)

def halstead_complexity(operators, operands, total_operators, total_operands):
    """ Dada la cantidad de operadores y operandos unicos (sin repeticiones), y la cantidad total de operadores y operandos (con repeticiones) se realizan los diferentes calculos de Halstead para medir complejidad:
		Vocabulario: vocabulary = operators + operands
		length: length = total_operators + total_operands
		Longitud calculada: calculated_length = operators*log(operators) + operands*log(operands)
		Volumen (describe el tamano de la implementacion de un algoritmo. Debe estar entre 20 y 1000 para una funcion/metodo): volume = length*log(vocabulary)
		Dificultad (nivel de dificultad para mantener, lo que lleva a mayor propension al error): difficulty = (operators/2)*(total_operands/operands) """
    halstead = Halstead()
    try:        
        halstead.vocabulary = operators + operands
        halstead.length = total_operators + total_operands
        
        if operators != 0 and operands != 0:
            halstead.calculated_length = operators*math.log(operators)+operands*math.log(operands)
        else:
            halstead.calculated_length = 0.0
            
        if halstead.vocabulary > 0:
            halstead.volume = halstead.length*math.log(halstead.vocabulary)
        else: 
            halstead.volume = 0.0
            
        if operands != 0:
            halstead.difficulty = (operators/2)*(total_operands/operands)
        else:
            halstead.difficulty = 0.0
           
    except ValueError:
        print("Error°. Valores: {0:4d}, {1:4d}, {2:4d}, {3:4d} ", operators, operands, total_operators, total_operands)
    return halstead
    
def calcular_complejidad(function_count, output, path ="."):
    """ realiza el reporte de complejidad para todos los archivos en un path determinado, aplicando la funcion establecida para contabilizar, y escribiendo el reporte en output"""
    with open(".\\log.txt","w") as log:
        os.chdir(path)
        path_corregido = os.getcwd()
        coleccion_contadores = []
        archivos = os.listdir()
        
        for archivo in archivos:
            if os.path.isdir(path_corregido + "\\" + archivo): #es un directorio, recorrerlo
                log.write("[DEBUG] Directorio: " + path_corregido + "\\" + archivo + "\n")
                os.chdir(path_corregido + "\\" + archivo)
                coleccion_contadores.extend(calcular_complejidad_int(function_count, path_corregido + "\\" + archivo, log))
            elif os.path.isfile(path_corregido + "\\" + archivo): #es un archivo, procesarlo
                coleccion_contadores.append(function_count(path_corregido + "\\" + archivo, log))
            else:
                log.write("[WARNING] " + path_corregido + "\\" + archivo + " no es un archivo\n")
                
        cant_archivos = 0
        
        halstead_obj = Halstead()
        
        with open(output,"w") as file:
            file.write("{0:60}|{1:25}|{2:25}|{3:25}|{4:25}|{5:25}|{6:25}|{7:25}|{8:25}|{9:25}|{10:25}|{11:25}|{12:25}|{13:25}|{14:25}\n".format("ARCHIVO","LINES", "EDGES", "NODES", "COMPONENTS", "OPERATORS", "OPERANDS", "TOT.OPERATORS", "TOT.OPERANDS", "CYCLOMATIC COMPLEX","HALSTEAD.VOCABULARY","HALSTEAD.LENGTH", "HALSTEAD.CALC.LENGTH", "HALSTEAD.VOLUME", "HALSTEAD.DIFFICULTY"))
            for c in coleccion_contadores:
                halstead_obj = halstead_complexity(c.operators, c.operands, c.total_operators, c.total_operands)
                cant_archivos+=1
                file.write("{0:60}|{1:25d}|{2:25d}|{3:25d}|{4:25d}|{5:25d}|{6:25d}|{7:25d}|{8:25d}|{9:25d}|{10:25d}|{11:25d}|{12:25}|{13:25}|{14:25}\n".format(c.archivo,c.lines, c.edges, c.nodes, c.components, c.operators, c.operands, c.total_operators, c.total_operands, cyclomatic_complexity(c.edges, c.nodes, c.components), halstead_obj.vocabulary, halstead_obj.length, halstead_obj.calculated_length, halstead_obj.volume, halstead_obj.difficulty))
        log.write("[INFO] " + repr(cant_archivos)+" archivos procesados.\n")
        
    print (repr(cant_archivos)+" archivos procesados.")
        

def calcular_complejidad_int(function_count, path, log_file):
    """ Función interna, para aplicar recursividad entre los directorios donde se encuentren los fuentes"""
    os.chdir(path)
    path_corregido = os.getcwd()
    coleccion_contadores = []
    archivos = os.listdir()
    
    for archivo in archivos:
        if os.path.isdir(path_corregido + "\\" + archivo): #es un directorio, entonces hay que recorrerlo
            log_file.write("[INFO] Directorio: " + path_corregido + "\\" + archivo + "\n")
            os.chdir(path_corregido + "\\" + archivo)            
            coleccion_contadores.extend(calcular_complejidad_int(function_count, path_corregido + "\\" + archivo, log_file))
        elif os.path.isfile(path_corregido + "\\" + archivo):  #es un archivo, procesarlo
            coleccion_contadores.append(function_count(path_corregido + "\\" + archivo, log_file))
        else:
            log_file.write("[ERROR] " + repr(sys.exc_info()[0]))
    
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

class Halstead:
    """ Clase que es utilizada para gestionar la información resultante de los cálculos de complejidad de Halstead"""
    vocabulary = 0
    length = 0
    calculated_length = 0.0
    volume = 0.0
    difficulty = 0.0
    
if __name__ == "__main__":
    import sys