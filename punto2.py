#Imports utilizados 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from networkx.algorithms import bipartite
from tkinter import Tk,Button,filedialog

class punto2:

    #Variables Globables
    file = np.loadtxt
    drFile = np.loadtxt
    
    def beatifulGraph():
        global file #Variables Globales
        global drFile #Variables Globales

        #Grafo 1 del ejercicio
        grafo = nx.Graph()
        grafo.add_nodes_from(file[0])
        dr1 = tuple(file[1])
        grafo.add_edges_from([dr1])
        
        #Grafo 2 del ejercicio
        grafo2 = nx.Graph()
        edges = tuple([tuple(e) for e in drFile])
        grafo2.add_node(drFile[0][0])
        grafo2.add_edges_from(edges)


        #Ejemplos -> Grafos creados para los ejemplos, tambien cargados desde archivo
        #Tambien se puede modificar la ruta de archivo, se dejan precargados para ser mas rapido los ejemplos
        e1 = np.loadtxt("./Archivos/ejemplo1.txt",dtype=int) #Ejemplo 1
        e1_skip = np.loadtxt("./Archivos/ejemplo1.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
        e2 = np.loadtxt("./Archivos/ejemplo2.txt",dtype=int) #Ejemplo 2
        e2_skip = np.loadtxt("./Archivos/ejemplo2.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
        e3 = np.loadtxt("./Archivos/ejemplo3.txt",dtype=int) #Ejemplo 3
        e3_skip = np.loadtxt("./Archivos/ejemplo3.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
        #Creacion de Grafos
        
        #Grafo 1
        eG = nx.Graph()
        eG.add_node(e1[0][0]) #Se accede al vertice de esta forma, ya que el archivo se carga como matriz
        eGc1 = tuple([tuple(e) for e in e1_skip])
        eG.add_edges_from(eGc1)
        
        #Grafo 2
        eG2 = nx.Graph()
        eG2.add_node(e2[0][0]) #Se accede al vertice de esta forma, ya que el archivo se carga como matriz
        eGc2 = tuple([tuple(e) for e in e2_skip])
        eG2.add_edges_from(eGc2)
        
        #Grafo 3
        eG3 = nx.Graph()
        eG3.add_node(e3[0][0]) #Se accede al vertice de esta forma, ya que el archivo se carga como matriz
        eGc3 = tuple([tuple(e) for e in e3_skip])
        eG3.add_edges_from(eGc3)

        #Comprobacion de bipartito
        #Aclaracion pusimos un layaout sobre algunos grafos en especifico para que muestre el diseño del grafo
        #En modelo bipartito
        print("\nResultado")
        if(bipartite.is_bipartite(grafo)):
            X,Y = bipartite.sets(grafo)
            #Se eleva al cuadrado cada uno de los elementos que contiene cada conjunto tanto X como Y
            #Y al final el resultado se suma, obteniendo asi el grafo bonito o BeatifulGraph
            print(2**len(X)+2**len(Y))  
            #Para poder tener una mejor posicion de cada vertice a la hora de mostrarlo en pantalla
            #Organizacion Pos para el Layout
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(X) )  
            pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
            nx.draw(grafo, pos=pos,node_color='Green',with_labels=True)
            plt.show()
        else:
            print(0)
        
        if(bipartite.is_bipartite(grafo2)):
            X,Y = bipartite.sets(grafo2)
            #Se eleva al cuadrado cada uno de los elementos que contiene cada conjunto tanto X como Y
            #Y al final el resultado se suma, obteniendo asi el grafo bonito o BeatifulGraph
            print(2**len(X)+2**len(Y))  
            #Para poder tener una mejor posicion de cada vertice a la hora de mostrarlo en pantalla
            #Organizacion Pos para el Layout
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(X) )  
            pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
            nx.draw(grafo2, pos=pos,node_color='Green',with_labels=True)
            plt.show()
        else:
            print(0)
        
        #Verifica si es bipartito pero para los ejemplos
        print("Ejemplos Aplicando el mismo metodo")
        if(bipartite.is_bipartite(eG)):
            X,Y = bipartite.sets(eG)
            #Se eleva al cuadrado cada uno de los elementos que contiene cada conjunto tanto X como Y
            #Y al final el resultado se suma, obteniendo asi el grafo bonito o BeatifulGraph
            print(2**len(X)+2**len(Y))  
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(X) )  
            pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
            nx.draw(eG, pos=pos,node_color='Grey',with_labels=True)
            plt.show()
        else:
            print(0)
        
        if(bipartite.is_bipartite(eG2)):
            X,Y = bipartite.sets(eG2)
            #Se eleva al cuadrado cada uno de los elementos que contiene cada conjunto tanto X como Y
            #Y al final el resultado se suma, obteniendo asi el grafo bonito o BeatifulGraph
            print(2**len(X)+2**len(Y))  
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(X) )  
            pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
            nx.draw(eG2, pos=pos,node_color='Pink',with_labels=True)
            plt.show()
        else:
            print(0)

        if(bipartite.is_bipartite(eG3)):
            X,Y = bipartite.sets(eG3)
            #Se eleva al cuadrado cada uno de los elementos que contiene cada conjunto tanto X como Y
            #Y al final el resultado se suma, obteniendo asi el grafo bonito o BeatifulGraph
            print(2**len(X)+2**len(Y))  
            pos = dict()
            pos.update( (n, (1, i)) for i, n in enumerate(X) )  
            pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 
            nx.draw(eG3, pos=pos,node_color='Blue',with_labels=True)
            plt.show()
        else:
            print(0)
        

    #Main
    if __name__ == '__main__':
        #Ventana del programa
        root = Tk()
        root.geometry('500x500')
        root.title('BUSCAR ARCHIVO')

        #Solicitud del archivo
        #Es recomendable o es lo mejor que seleccione el archivo punto2.txt para un correcto funcionamiento del programa

        def searchFile():
            searchFile = filedialog.askopenfilename()
            global file
            global drFile
            file = np.loadtxt(searchFile,dtype = int,max_rows=2)
            drFile = np.loadtxt(searchFile,dtype = int,skiprows=2)
           
        

        #Ejecuta la funcion principal
        def graphFunction():
            global beatifulGraph
            beatifulGraph()
        
        #Botones
        buttonSearchFile = Button(root,text='Buscar Archivo Principal',bg="Cyan",command=searchFile)
        buttonSearchFile.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.10)
        #Boton para mostrar el grafo y realizar la operacion
        buttonGraficar = Button(root,text='Realizar operacion',bg="Cyan",command=beatifulGraph)
        buttonGraficar.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.10)

        root.mainloop()


