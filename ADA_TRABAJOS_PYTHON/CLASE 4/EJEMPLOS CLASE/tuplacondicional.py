#Crear una tupla con varios elementos
mi_tupla = (10, 20, 30, 40, 50)

#Encontrar la posicion del numero 30 en la tupla.
indice_de_30 = mi_tupla.index(30)

#Mostrar el resultado
print("El numero 30 se encuentra en la posicion", indice_de_30, "de la tupla.")

#Explicacion
#En la tupla (10, 20, 30, 40, 50), el numero 30 esta en la posicon 2
#El metodo index (30) devuelve 2, que es el indice del primer valor 30 en la tupla.

#Verificar si un valor esta en la tupla antes de buscar su indice
valor_buscado = 60
if valor_buscado in mi_tupla:
    #Si el valor esta en la tupla, encontrar su indice.
    print(f"El numero {valor_buscado} se encuentra en la posicion {indice_del_valor} de la tupla.")
else:
    #si el valor no esta en la tupla, mostrar un mensaje
    print(f"El numero {valor_buscado} no esta en la tupla.")

#Explicacion:
#primero verificamos si el valor 60 esta en la tupla usando 'in'.
#Si esta, usamos 'index' para encontrar su posicion 
#si no esta, mostramos un mensaje indicando que el valor no se encuentra en la tupla.