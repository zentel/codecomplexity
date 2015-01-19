#code_complexity_PL_SQL

import code_complexity

def count_PL(file_name, log_file):
    """ Cuenta los elementos en un archivo PL para poder realizar los calculos de complejidad """
    # operadores de PL_SQL para contar dentro del código
    PL_SQL_operators = "+ - * / ** = != <> ~= < > >= <= LIKE BETWEEN IN ISNULL AND OR NOT DECLARE BEGIN END IF THEN ELSE CASE WHEN WHILE FOR CREATE REPLACE TYPE PROCEDURE EXEC DROP SELECT UPDATE DELETE FUNCTION RETURN AS END FROM WHERE ORDER BY RECORD EXCEPTION TRIGGER PACKAGE BODY LOOP ROLLBACK SAVEPOINT COMMIT SCALAR LOB NUMERIC CHARACTER BOOLEAN DATETIME PLS_INTEGER BINARY_INTEGER BINARY_FLOAT BINARY_DOUBLE NUMBER DEC DECIMAL DOUBLE FLOAT INT INTEGER SMALLINT REAL CHAR VARCHAR2 RAW NCHAR NVARCHAR2 LONG RAW ROWID UROWID TABLE YEAR MONTH DAY HOUR MINUTE SECOND TIMEZONE BFILE BLOB CLOB NCLOB CONSTANT GROUP ("
    
    cont = code_complexity.Contadores()
    path_set = file_name.split("\\") 
    cont.archivo = path_set[len(path_set)-1]
    cont.lines = 0
    linea = ""
    elementos = {}
    PL_operators_list = PL_SQL_operators.split(" ")
    
    with open(file_name) as arq:
        try:
            linea = arq.readline()
        except UnicodeDecodeError:
            log_file.write("[ERROR] Error de codificación Unicode en archivo " + file_name + "\n")
        
        while(linea != ""):
            try:
                linea = arq.readline()
                cont.lines = cont.lines + 1
                linea = linea.upper()
                linea = linea.replace(",", "")
                linea = linea.replace(";", "")
                linea = linea.replace(":", "")
                #linea = linea.replace("\n", "")
                
                splitted = linea.split(" ")
                for o in splitted:
                    cleaned_o = o.replace("\n", "")
                    cleaned_o = cleaned_o.replace("\t","")
                    if cleaned_o in elementos:
                        elementos[cleaned_o] += 1
                    else:
                        elementos[cleaned_o] = 1
                        
            except UnicodeDecodeError:
                log_file.write("[ERROR] Error de codificación Unicode en archivo " + file_name + "\n")
                
        for k in elementos.keys():
            cleaned_k = k.replace("\n", "")
            cleaned_k = cleaned_k.replace("\t","")
                        
            if cleaned_k in PL_operators_list:
                try:
                    log_file.write("[DEBUG] key encontrada en el archivo {0} es {1} y representa {2}\n".format(file_name, repr(cleaned_k),"operador"))
                except:
                    log_file.write("[ERROR] generando log")
                    
                cont.operators +=1
                cont.total_operators += elementos[cleaned_k]
            else:
                try:
                    log_file.write("[DEBUG] key encontrada en el archivo {0} es {1} y representa {2}\n".format(file_name, repr(cleaned_k),"operando"))
                except:
                    log_file.write("[ERROR] generando log")
                    
                cont.operands +=1
                cont.total_operands += elementos[cleaned_k]
        
        #Valores para la complejidad ciclomática
        #Por defecto, hay un path y un nodo para recorrer
        cont.edges = 1
        cont.nodes = 1
        
        if "WHEN" in elementos.keys(): #el when agrega un nodo y dos paths
            cont.edges += elementos["WHEN"] * 2
            cont.nodes += elementos["WHEN"] 
            
        if "IF" in elementos.keys(): #el if agrega un nodo y dos paths
            cont.edges += elementos["IF"] * 2
            cont.nodes += elementos["IF"] 
            
        if "CASE" in elementos.keys(): #el case agrega un nodo y un paths
            cont.edges += elementos["CASE"]
            cont.nodes += elementos["CASE"] 
            
        if "EXCEPTION" in elementos.keys(): #el exception agrega un nodo y dos paths
            cont.edges += elementos["EXCEPTION"] * 2
            cont.nodes += elementos["EXCEPTION"]
            
        if "EXEC" in elementos.keys(): #el exec agrega un nodo y un paths
            cont.edges += elementos["EXEC"]
            cont.nodes += elementos["EXEC"] 
            
        if "FOR" in elementos.keys():  #el for agrega un nodo y dos paths
            cont.edges += elementos["FOR"] * 2
            cont.nodes += elementos["FOR"] 
            
        if "WHILE" in elementos.keys(): #el while agrega un nodo y dos paths
            cont.edges += elementos["WHILE"] * 2
            cont.nodes += elementos["WHILE"] 
            
        if "(" in elementos.keys(): #el parentesis agrega un nodo y dos paths
            cont.edges += elementos["("] * 2
            cont.nodes += elementos["("] 
            
        if "ELSE" in elementos.keys(): # el ELSE agrega un nodo y un paths
            cont.edges += elementos["ELSE"]
            cont.nodes += elementos["ELSE"]
        
        if "BEGIN" in elementos.keys(): # el begin agrega un nodo y un paths (ademas de un elemento)
            cont.edges += elementos["BEGIN"]
            cont.nodes += elementos["BEGIN"]
            cont.components += elementos["BEGIN"]
        else:
            cont.components = 1
            
        if "PROCEDURE" in elementos.keys(): # el begin agrega un nodo y un paths (ademas de un elemento)
            cont.edges += elementos["PROCEDURE"]
            cont.nodes += elementos["PROCEDURE"]
            cont.components += elementos["PROCEDURE"]
        else:
            cont.components = 1
            
        if "FUNCTION" in elementos.keys(): # el begin agrega un nodo y un paths (ademas de un elemento)
            cont.edges += elementos["FUNCTION"]
            cont.nodes += elementos["FUNCTION"]
            cont.components += elementos["FUNCTION"]
        else:
            cont.components = 1    
        
            
        if "WHERE" in elementos.keys(): 
            cont.edges += elementos["WHERE"] + cont.operands #en el caso de selects, la complejidad viene dada por la cantidad de variables que se manejan
            cont.nodes += elementos["WHERE"]
            
    return cont
    
    