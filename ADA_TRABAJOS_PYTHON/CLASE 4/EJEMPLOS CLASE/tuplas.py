#crear una tupla con varios tipos de datos: uns numero entero, una cadena de texto y un numero decimal
tupla_mixta = (1, "Hola", 3.5)

#Mostrar la tupla completa en pantalla
print('Tupla completa:', tupla_mixta)

#Acceder a los elementos de la tupla por su indice (posicion)
print('Primer elemento de la tupla:', tupla_mixta[0]) # imprime: 1
print('segundo elemento de la tupla:', tupla_mixta[1]) #imprime: "Hola"
print("tercer ellmento de la tupla:",tupla_mixta[2]) #Imprime 3.5

#Explicar que las tuplas son inmutables, es decir, no se pueden cambiar sus elementos
print("\n Las tuplas no se pueden modificar. Intentemos cambiar el primer elemento de la tupla:")

#Ejemplo de intento de cambio que causaria un error (no ejecutar esta linea)
# tupla_mixto [0] = 10 # Esto causara un error por que las tuplas no permiten cambios

#Explicacion clara de inmutabilidad
print("Si intentamos hacer 'tupla_mixta[0]=10)',") #un solo print con el de abajo
print("Python mostrara un error por que no se puede cambiar ningun elemento de una tupla.")

#Mostras como podemos "modificar"creando una nueva tupla en vez de intentar cambiar la original
nueva_tupla = (10,"hola",3.5) #creamos una nueva tupla con el primer valor modificado

#mostrar la nueva tupla
print("Nueva tupla con el primer elemento cambiado:", nueva_tupla)

#Mostrar que la tupla orignal permanece igual
print('Tupla original permanece sin cambios:', tupla_mixta)
