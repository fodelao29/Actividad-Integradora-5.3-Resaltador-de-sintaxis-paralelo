# Actividad Integradora 5.3 Resaltador de sintaxis paralelo usando multiprocesos

# Rodolfo De la O Pérez 			ID: A01366363
# Santiago Alberto Sorzano Mongel	ID: A01769673 

import glob
import multiprocessing
import dominate
from dominate.tags import *
import re
import time
import threading 

def Resaltador(textoEntrada, HTML_Salida):
    # Archivos de entrada
    expresionesRegulares = "palabrasreservadas.txt"
    archivoEstilo = "estilo.css"

    # En esta sección se separan el tipo de expresiónes regulares que hay en el archivo de las palabras reservadas.
    ## Utilizamos un .txt en donde estan todas las palabras reservadas que toma como referencia para resaltarlas.
    variables = ""
    operadores = ""
    enteros = ""
    flotante = ""
    #numeros = ""
    strings = ""
    comentarios = ""
    comentariosmul = ""
    Palabras_Reservadas = ""
    
    lexico = [variables,operadores,enteros,flotante,strings,comentarios,comentariosmul,Palabras_Reservadas]

    with open(expresionesRegulares,"r") as archivo:
        expresiones = archivo.readlines()
        i = 0
        for linea in expresiones:
            lexico[i] = linea.rstrip()
            i += 1
    archivo.close()

    ruta = dominate.document(title="Resaltador de sintaxis")

    with ruta.head:
        link(rel="stylesheet", href=archivoEstilo)
        meta(charset = "UTF-8")

    with ruta:
        body(cls = "estilo_general")
        with open(textoEntrada,"r",encoding = "utf8") as input:
            archivo = input.readlines()
            i=0

            for linea in archivo:
                with div():
                    attr(cls='estilo_general')
                    k = 0

                    while(linea[k] == " "):
                        span("_", cls = "espacio")
                        k += 1

                    archivo[i] = linea.rstrip()
                    renglon = archivo[i].rsplit()
                    j = 0 

                    if (re.match(lexico[3],archivo[i])):
                        span(archivo[i],cls = "comentarios")
                    else:
                        for palabra in renglon:
                            if (re.match(lexico[0],palabra)):
                                span(palabra,cls = "operadores")
                            elif (re.match(lexico[1],palabra)):
                                span(palabra,cls = "numeros")
                            elif(re.match(lexico[2],palabra)):
                                span(palabra,cls = "strings")
                            elif(re.match(lexico[4],palabra)):
                                span(palabra, cls = "Palabras_Reservadas")
                            else:
                                try:
                                    if (renglon[j + 1] == '('):
                                        span(palabra,cls = "funcion")
                                    else:
                                        span(palabra)
                                except:
                                    span(palabra)
                            j += 1
                i += 1
        input.close()

    # En esta sección usamos "w" o "a" para que en caso de que 
    #no exista tal html, lo cree, escriba en el y despues lo cierre.
    html = open(HTML_Salida,"w",encoding = "utf8")
    html.write(str(ruta))
    html.close()

if __name__ == "__main__": 

    directorio = str(input("Ingresa el directorio (utiliza  dash [/] para las separaciones) ./ para analizar el directorio actual : "))
    #Este es el tipo de estensión que el programa va a buscar
    #dentro de la carpeta que se mencione en la terminal.
    #En este caso utilizamos extensiones para python, css, c++, javascript y archivos txt.
    extensiones = ["/**/*.py","/**/*.css","/**/*.c","/**/*.js","/**/*.txt"] 
    archivos = [] #Aqui es donde se guardaran todos los archivos ecnotnrados con las extensiones antes mencionadas.

    for arch in extensiones:
        nuevo_archivo = glob.glob(directorio + arch, recursive=True) 
        archivos += nuevo_archivo 

    processes = [None] * len(archivos) 

    tiempoInicial = time.time()

    for i, f in enumerate(archivos): 
        processes[i] = threading.Thread(target=Resaltador, args=(str(archivos[i]), "./ejemplos/archivo" + str(i) + ".html"))
        #En la linea anterior se crea un html para cada archivo encontrado, todos con el mismo nombre seguido de 1,2,3 sucesivamente.

    for p in processes: # Iniciando los procesos
        p.start()

    for p in processes: # Esperamos a que terminen
        p.join()

    tiempoFinal = time.time()

    tiempoEjecucion = tiempoFinal - tiempoInicial

    print("\n"*5)
    print("*"*58)
    print("EL TIEMPO DE EJECUCIÓN FUE: ",tiempoEjecucion, "SEGUNDOS.")
    print("*"*58)
    print("\n"*5)
