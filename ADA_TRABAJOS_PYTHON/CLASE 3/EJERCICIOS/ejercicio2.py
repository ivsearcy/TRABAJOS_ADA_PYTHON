#Ejercicio Suma de Sublistas

#INSTRUCCION: Crea un programa que tome una lista de números y calcule la suma de una sublista especificada por el usuario.

#PASO 1. Define una lista de números predefinida.
mi_lista = [1,2,3,4,5,6,7,8,9,10]
#Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.
print('Tengo una lista del 1 al 10. Haremos una sublista para ti y me ayudarás a definirla de la siguiente manera: ')
indice_inicio = int(input("1. Elige un número del 1 al 5: "))
indice_fin =  int(input("2. Elige un número del 6 al 10: "))
#Usa slicing para obtener la sublista.
lista_new = mi_lista[indice_inicio:indice_fin]
print("Tu lista es: ", lista_new)
# #Suma los elementos de la sublista.
suma = sum(lista_new)
#Muestra la suma.
print('La suma de los números en tu lista es:', suma)


