#Creamos diccionario
estudiante = {
    "nombre" : "Laura",
    "edad" : 22,
    "curso" : "Ingeniria",
    "ciudad" : "Barcelona"
}

#Imprimos el diccionario
print("Diccionario original: ", estudiante)

#Eliminar el elemnto con la clave 'curso' usando del
del estudiante["curso"]

#Imprimimos el diccionario despues de eliminar curso
print("Diccionario despues de eliminar curso: ", estudiante)