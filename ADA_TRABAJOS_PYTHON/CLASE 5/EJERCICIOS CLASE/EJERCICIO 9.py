# Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado.
#PASO #1. Crea un diccionario que represente una clase con los siguientes datos:
# nombre_clase, o estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad).
clase = {"nombre_clase" : "Matematicas",
         "estudiantes" : [{"nombre" : "Ada Lopez", "edad" : 10},
                          {"nombre" : "Juan Camarena", "edad" : 9},
                          {"nombre" : " Karla Alvarez", "edad" : 9}]
}
print(clase)

# PASO 2. Escribe una función que busque la edad de un estudiante dado su nombre 
# usando el índice de la lista en lugar de bucles (suponiendo que conoces el índice).

# PASO 3. Imprime la edad del estudiante buscado.