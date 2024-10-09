# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario


#PASO 1. Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968.
libro = {
    "Titulo" : "Pedro Paramo",
    "Autor" : "Juan Rulfo",
    "Año de publicacion" : 1955,
    "Genero" : "Novela",
    "Año de publicacion" : 1968
}
print("Tu libro se actualizo:", libro)

#PASO 2. Elimina el género del diccionario.
del libro ["Genero"]

print("Tu libro sin genero", libro)

#PASO 3. Imprime el diccionario después de cada operación