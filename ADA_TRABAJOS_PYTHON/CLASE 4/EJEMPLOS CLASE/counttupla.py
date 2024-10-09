#Crear una tupla con elementos repetidos
mi_tupla= (1, 2, 3, 1, 4, 1, 5)

#Contar cuantas veces aparece el numero 1 en la tupla
numero_de_unos = mi_tupla.count(1)

#Mostrar el resultado
print("El numero 1 aparece", numero_de_unos, "veces en la tupla.")

#Explicacion:
#La tupla(1, 2, 3, 1, 4, 1, 5) contiene el numero 1 tres veces.
#El metodo count(1) cuenta estas apariciones y devuelve 3.

#Contar cuantas veces aparece el numero 7 en la tupla
numero_de_siete = mi_tupla.count(7)

#Mostrar el resultado
print("El numero 7 aparece", numero_de_siete, "veces en la tupla." )

#Explicacion:
#El numero 7 no esta en la tupla, por lo que el metodo count devuelve 0