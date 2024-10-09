# 1. Declaracion de variables y constantes
edad=25 #numero
nombre= "Ana" #cadena de texto (string)
esta_estudiando=True #booleano

#declaracion de constantes
PI=3.14 #numero
PAIS= "ARGENTINA" #CADENA DE TEXTO (STRING)

#2. lEER VALORES POR TECLADO
edad=int(input("Introduce tu edad: ")) # Leer un numero entero
nombre= input("introduce tu nombre: ") #leer una cadena de texto
esta_estudiando=input("¿estás estudiando? (si/no): ").lower ()=="si" #leer y convertir a booleano

#3.Tipos de Datos
cantidad_de_libros=10 #numero (int)
titulo_libro="El principito" #cadena de texto(string)
es_interesante= True #booleano(bool)
temas=['Aventura', "Fantasia", "Filosofia"] #lista (array)
autor={"nombre": "Antoine de Saint-Exupery", "nacionalidad": "Francesa"} #diccionario (objeto)

#Convertir tipos de datos
edad_str=('edad') #convertir numero a cadena de texto
cantidad_de_libros_float= float(cantidad_de_libros) #convertir entero a numero de punto flotante

#4.Imprimir Resultados en la Consola
print ("Nombre:", nombre)
print("Edad:",edad)
print("¿Está estudiando?", esta_estudiando)
print("constante PI:",PI)
print('Constante Pais:', PAIS)
print ("Cantidad de libros:", cantidad_de_libros)
print ("Titulo del libro:", titulo_libro)
print("¿Es interesante?", es_interesante)
print ('Temas del libro', temas)
print ("Autor del libro:", autor)
print("edad(como cadena de texto):", edad_str)
print('cantidad de libros(como float):', cantidad_de_libros_float)
