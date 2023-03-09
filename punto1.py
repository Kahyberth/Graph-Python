import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

'''
 ▁▂▃▅▇Variables▇▆▅▃▂
grafo = representa el grafo creado con la libreria networkx
vertices = representa los vertices 
aristas = las conextiones con los vertices
com = es la comprension de las lista para convertirla en tuplas
dfsR = es el resultado de la busqueda por profundidad que nos ofrece networkx
resultado = es una lista la cual se encarga de guardar el resultado final

▁▂▃▅▇Procedimiento▇▆▅▃▂
Primero se cargan los archivos con ayuda de la libreria numpy.loadtxt,
despues se dibuja el grafo usando la libreria networkx se realiza una comprension de listas
para convertir su contenido en tuplas para asi poder ser usado como conexion entre los vertices
o Edges, una vez graficado al cerrar la ventana que muestra el grafo
se le realiza la busqueda por DFS usando la libreria networkx retornando asi el resultado.

'''

class algoritmo:
   def punto1(archivo,root):
      #Manipulacion de Archivos
      file = np.loadtxt(archivo,dtype=int,skiprows=1)
      e1 = np.loadtxt("./Archivos/ejemplo1.txt",dtype=int) #Ejemplo 1
      e1_skip = np.loadtxt("./Archivos/ejemplo1.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
      e2 = np.loadtxt("./Archivos/ejemplo2.txt",dtype=int) #Ejemplo 2
      e2_skip = np.loadtxt("./Archivos/ejemplo2.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
      e3 = np.loadtxt("./Archivos/ejemplo3.txt",dtype=int) #Ejemplo 3
      e3_skip = np.loadtxt("./Archivos/ejemplo3.txt",dtype=int,skiprows=1) #Representa el delimitador o salto de fila desde donde inicia
      
      #Creacion del Grafo
      grafo = nx.Graph()
      grafo = grafo.to_undirected()
      aristas = tuple([tuple(e) for e in file])
      grafo.add_node(file[0][0])
      grafo.add_edges_from(aristas)
      #print(aristas) #Aristas 
      #Dibuja el grafo
      nx.draw(grafo,pos=nx.spring_layout(grafo),with_labels=True,node_color='Blue')
      #plt.legend()
      plt.show()

   
      #Ejemplos para probar el algoritmo
      
      #Cracion de los grafos
      #Grafo 1
      eG = nx.Graph()
      eG.add_node(e1[0][0])
      eGc1 = tuple([tuple(e) for e in e1_skip])
      eG.add_edges_from(eGc1)
       
       #Grafo 2
        
      eG2 = nx.Graph()
      eG2.add_node(e2[0][0])
      eGc2 = tuple([tuple(e) for e in e2_skip])
      eG2.add_edges_from(eGc2)
      #Grafo 3
        
      eG3 = nx.Graph()
      eG3.add_node(e3[0][0])
      eGc3 = tuple([tuple(e) for e in e3_skip])
      eG3.add_edges_from(eGc3)

      
   
      #Dibujado los grafos de los ejemplos
      nx.draw(eG,pos=nx.spring_layout(eG),with_labels=True,node_color="Green")
      #plt.legend()
      plt.show()
   
      nx.draw(eG2,pos=nx.spring_layout(eG2),with_labels=True,node_color="red")
      #plt.legend()
      plt.show()

      nx.draw(eG3,pos=nx.spring_layout(eG3),with_labels=True,node_color="purple")
      #plt.legend()
      plt.show()


      #Busqueda por profundidad
      resultado = [] #Se encarga de guardar el resultado
      dfsR = nx.dfs_tree(grafo,root)
      for i in dfsR:
         resultado.append(i) #Agrega el resultado encontrado por cada iteracion que hace el bucle
      print("Resultado -->",resultado)
      resultado.clear() #Reinicio la lista

      #Busqueda por profundidad para los ejemplos
      dfsR1 = nx.dfs_tree(eG,5)
      dfsR2 = nx.dfs_tree(eG2,4)
      dfsR3 = nx.dfs_tree(eG3,3)
      for i in dfsR1:
         resultado.append(i)
      print("Resultado ejemplo #1 -->",resultado)
      resultado.clear() #Reinicio la lista

      for i in dfsR2:
         resultado.append(i)
      print("Resultado ejemplo #2 -->",resultado)
      resultado.clear() #Reinicio la lista

      for i in dfsR3:
         resultado.append(i)
      print("Resultado ejemplo #3 -->",resultado)   

   #MAIN
   if __name__ == '__main__':
       #conexAristas.txt = las aristas o conexiones con los vertices
       #root = la raiz recibe un entero ejmp: 1
       #Ahorro de trabajo -> 
       # archivo = ./Archivos/conexAristas.txt
       # root = 1
       #Ejemplo de uso
       #print(punto1("./Archivos/conexAristas.txt",1))
     # archivo = input("Ingrese el archivo (Archivon txt): ")
     # root = int(input("Ingrese el numero de la raiz (int): "))
      #La ruta se puede cambiar
      print(punto1("./Archivos/conexAristas.txt",1))
   
