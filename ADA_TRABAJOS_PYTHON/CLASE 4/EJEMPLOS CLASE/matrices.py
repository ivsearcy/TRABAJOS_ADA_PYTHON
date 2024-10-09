#Definimos una matriz de 3 x 3
matriz =[ 
         [1, 2, 3], #fila 0
         [4, 5, 6], #fila 1
         [7, 8, 9]  #fila 2
]

#acceder y mostrar algunos elementos especificos de la matriz
print('Algunos elementos de la matriz:')
print('elemento en fila 0, columna 0:', matriz[0][0] ) #elemnto en fila 0, columna 0(1)
print ('Elemento en fila 1, columna 2:', matriz[1][2]) #elemento en fila 1, columna 2(6)

#modificar elementos especificos de la matriz
matriz[0][1] = 10 #cambiar el elemento en fila 0, columna 1 por 10
matriz[2][0] = 15 #cambiar el elemento en fila 2, columna 0 por 15
print("matriz despues de las modificaciones:")
print(matriz) #imprime la matriz completa despues de las modificaciones

#acceder a una fila completa
print("*\nAccediendo a una fila completa:")
fila_completa = matriz[1] #obtener toda la segunda fila
print('Fila completa en la posicion 1:', fila_completa) #imprime [4,5,6]

#Reemplazar una fila completa
print("*\nReemplazando una fila completa:")
matriz[1] = [20,21, 22] #Reemplazar la segunda fila con nuevos valores
print("Matriz despues de reemplazar la fila 1: ")
print(matriz) #imprime la matriz completa despues de reemplazar la fila

#trabajar con una submatris(parte de la matriz)
print("*\nTrabajando con una submatriz")
submatriz = [matriz[0][1:3], matriz[1][1:3]] #extraer submatriz de las columnas 1 a 2 de las filas 0 y 1

#Mostrar toda la matriz al final
print("\nMatriz completa al final:")
print(matriz[0]) #imprime la primera fila
print(matriz[1]) #imprime la segunda fila
print(matriz[2]) #imprime la tercera fila


