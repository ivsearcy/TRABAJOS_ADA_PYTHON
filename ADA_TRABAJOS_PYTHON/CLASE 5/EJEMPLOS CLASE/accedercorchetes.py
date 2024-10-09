#Crear un diccionario con informacion de una persona
persona = {
    "nombre": 'Catalina',
    'edad' : 33,
    'ciudad' : 'Bogota'
}

#Acceder a los elemento susando corchetes
nombre = persona['nombre']
edad = persona['edad']
ciudad = persona ['ciudad']

#imprimir los valores
print("Nombre:", nombre)
print('Edad:', edad)
print('Ciudad:', ciudad)

#Intentar acceder a una clave que no existe
#print(persona['pais'])