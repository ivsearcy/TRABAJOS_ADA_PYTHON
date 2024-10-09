#Ejercicio 8: Modificar un Valor en un Diccionario Anidado
#PASO 1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves:
# nombre_tienda,  libros, que es una lista de diccionarios, donde cada diccionario representa un libro con 
# claves titulo y precio.

tienda = { "nombre_tienda" : "libreria Lector Feliz",
          "libros" : [{"titulo" : "recetas faciles", "precio" : 138},
                      {"titulo" : " programacion avanzada", "precio" : 160},
                      {"titulo" : "Cuentos infantiles", "precio" : 100}
                      ]}

print(tienda)

# PASO2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99).
#PASO 3. Imprime el título y el precio del segundo libro después de la modificación.