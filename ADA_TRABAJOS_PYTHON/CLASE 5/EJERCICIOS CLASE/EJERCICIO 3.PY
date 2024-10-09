#Ejercicio 3: Anidación Básica de Diccionarios
#PASO 1. Crea un diccionario que represente una persona con las siguientes claves:
# Nombre, Edad, Dirección (donde la dirección es otro diccionario con claves: 
persona = {
    "nombre" : "Paul",
    "edad" : 33,
    "direccion" : {
        "calle" : "Aldama",
        "ciudad" : "Ensenada",
        "codigo postal" : 22840
    }
}
print(persona)
# Calle, Ciudad, Código postal
#PASO 2. Imprime la ciudad de la dirección.
print("Ciudad", persona["direccion"]["ciudad"])




