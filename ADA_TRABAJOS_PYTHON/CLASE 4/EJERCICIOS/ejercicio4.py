#Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
#PASO 1. Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
frutas=("manzana", "banana", "cereza")

#PASO 2.Usa el método index para encontrar la posición de la fruta "banana".
banana = frutas.index("banana")
print("la posición de la fruta banana es", banana)

#PASO 3. Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.
busco = 'naranja'
if busco in frutas:
    print( "La fruta", {busco} ,"se encuentra en la tupla")
else:
    print("la fruta", {busco}, "no se encuentra en la tupla")
    