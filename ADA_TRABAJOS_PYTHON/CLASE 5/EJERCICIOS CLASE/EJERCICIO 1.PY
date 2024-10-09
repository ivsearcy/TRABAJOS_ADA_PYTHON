#Ejercicio 1: Crear y Acceder a un Diccionario Básico

#PASO 1. Crea un diccionario que contenga la siguiente información sobre un libro: 
# Título, Autor Año de publicación Género
libro = {
    "Titulo" : "Pedro Paramo",
    "Autor" : "Juan Rulfo",
    "Año de publicacion" : 1955,
    "Genero" : "Novela"
}
#PASO 2. Accede e imprime cada uno de estos valores usando las claves correspondientes.
titulo = libro["Titulo"]
autor = libro["Autor"]
año = libro['Año de publicacion']
genero = libro["Genero"]

print("Titulo: ", titulo)
print("Autor: ", autor)
print('Año: ', año)

