#Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado
#PASO1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores.
# Cada jugador es un diccionario con las claves: nombre y edad.
clubes = { "deportivo1" : [ 
                          {"nombre" : "Juan Perez",
                           "edad" : 35},
                           {"nombre" : " Luis Aldama",
                           "edad" : 34},
                           ],
            "deportivo 2" : [ {"nombre" : "Adrian Juarez", "edad" : 28}, {"nombre" : "Bruno Soto", "edad": 28}],
            "deportivo 3" : [{ "nombre" : "Gustavo Amador", "edad" : 25}, {"nombre" : "Vicente Aldrete", "edad" : 26}]
}
print(clubes)

#PASO 2. Cuenta cuántos jugadores en total tienen cada uno de los clubes