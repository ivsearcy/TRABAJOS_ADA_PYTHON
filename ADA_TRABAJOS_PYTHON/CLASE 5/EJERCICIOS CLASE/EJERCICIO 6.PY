#Ejercicio 6: Anidación Compleja de Diccionarios y Listas

#PASO1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene:
# Nombre, Año de fundación, Lista de clases, donde cada clase es un diccionario con:
# Nombre de la clase, Lista de estudiantes, donde cada estudiante es un diccionario con:
# Nombre, ▪ Edad

escuela={
    "nombre" : "Juan Escutia",
    "fundacion" : 1980, 
    "clases" : {
        "español" : [{
                         "nombre": "Elisa Lopez",
                         "edad" : 13
                      },
                     {
                         "nombre" : " Alejandro Perez",
                         "edad" : 12
                     },
                     {
                         "nombre" : "Adriana Ortiz",
                         "edad" : 14
                     }]
    }
}

print(escuela)
# #PASO 2. Imprime el nombre del primer estudiante de la primera clase.

