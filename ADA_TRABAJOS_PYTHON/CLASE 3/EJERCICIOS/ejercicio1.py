#Este es un ejercicio para contabilizar numeros especificos.

#PASO 1. PREDEFINIR LISTA DE NUMEROS
lista_numeros = [1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10,10,10]

#PASO2. SOLICITAR AL USUARIO QUE INGRESE UN NUMERO A BUSCAR
buscar = int(input('Tengo una lista de número del 1 al 10 que se repiten varias veces. Elige un número del 1 al 10 para saber cuantas veces se repite en la lista:'))
print('El numero que elgiste es:', buscar)
contar=lista_numeros.count(int(buscar))
print ("Se repite",contar, "veces")
                           



