import glob
import multiprocessing
import dominate
from dominate.tags import *
import re
import time
import threading

def Resaltador(textoEntrada, HTML_Salida):
    # Archivos de entrada
    expresionesRegulares = "expresionesFinal.txt"
    archivoEstilo = "estilo.css"

    # Se crean los léxicos que se tomarán del archivo de texto
    operadores = ""
    numeros = ""
    strings = ""
    comentarios = ""
    Palabras_Reservadas = ""
    lexico = [operadores,numeros,strings,comentarios,Palabras_Reservadas]

    # El archivo con las expresiones regulares se abre y se guardan las expresiones
    # El txt está ordenado de la siguiente forma:
    # Línea 1: Operadores
    # Línea 2: Numeros
    # Línea 3: Strings
    # Línea 4: Comentarios
    # Línea 5: Palabras reservadas
    with open(expresionesRegulares,"r") as archivo:
        expresiones = archivo.readlines()
        i = 0
        for linea in expresiones:
            lexico[i] = linea.rstrip()
            i += 1
    archivo.close()

    # Se crea el documento que servirá como guía para el HTML que resaltará la sintáxis
    guia = dominate.document(title="Resaltador de sintaxis")

    with guia.head:
        link(rel="stylesheet", href=archivoEstilo)
        meta(charset = "UTF-8")

    with guia:
        body(cls = "estilo_general")
        with open(textoEntrada,"r",encoding = "utf8") as input:
            archivo = input.readlines()
            i=0

            # En este for se checan las líneas enteras
            for linea in archivo:
                with div():
                    attr(cls='estilo_general')
                    k = 0

                    # Se toman en cuenta las indentaciones
                    while(linea[k] == " "):
                        span("_", cls = "espacio")
                        k += 1

                    archivo[i] = linea.rstrip()
                    renglon = archivo[i].rsplit()
                    j = 0 

                    if (re.match(lexico[3],archivo[i])):
                        span(archivo[i],cls = "comentarios")
                    else:
                        # En este for se checan las palabras de forma individual
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
                        # Termina for palabra in renglon
                i += 1
            # Termina for linea in archivo
        input.close()

    # Se crea el archivo HTML
    html = open(HTML_Salida,"w",encoding = "utf8")
    html.write(str(guia))
    html.close()

if __name__ == "__main__": # Esta parte del código corre sólo en la rama principal

    directorio = str(input("Ingresa el directorio (utiliza  dash [/] para las separaciones) ./ para analizar el directorio actual : "))

    extensiones = ["/**/*.py","/**/*.txt","/**/*.m"] # Extensiones buscadas
    archivos = [] # Array de archivos

    for arch in extensiones:
        nuevo_archivo = glob.glob(directorio + arch, recursive=True) # Busca los archivos
        archivos += nuevo_archivo 

    processes = [None] * len(archivos) # Crea un array con un tamaño igual al número de archivos encontrados

    tiempoInicial = time.time()

    for i, f in enumerate(archivos): # Crea un proceso para cada archivo y corre la función resaltadora
        processes[i] = threading.Thread(target=Resaltador, args=(str(archivos[i]), "./resaltado" + str(i) + ".html"))

    for p in processes: # Inicia cada proceso
        p.start()

    for p in processes: # Espera a que todos los procesos terminen
        p.join()

    tiempoFinal = time.time()

    tiempoEjecucion = tiempoFinal - tiempoInicial

    print("El tiempo de ejecución fue: ",tiempoEjecucion, "s")