#Ejercicio 1: Operaciones Básicas con Tuplas
#PASO 1: Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25).
mi_tupla = (5, 10, 15, 20, 25)
#PASO 2: Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
cuenta_el_diez= mi_tupla.count(10)

#PASO 3: Usa el método index para encontrar la posición del número 20 en la tupla.
indice_del_veinte = mi_tupla.index(20)

#PASO 4: Muestra los resultados de las operaciones anteriores.
print("el numero 10 se encuentra", cuenta_el_diez, "veces")
print("la posicion del 20 es:", indice_del_veinte)
