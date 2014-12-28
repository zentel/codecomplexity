#code_complexity_PL_SQL

import code_complexity

def count_PL(file_name):
    """ Cuenta los elementos en un archivo PL para poder realizar los calculos de complejidad """
    cont = Contadores()
    
    with open(file_name) as arq:
        linea = arq.readline()
        while(linea != ""):
            linea = arq.readline()

    return cont
    
    