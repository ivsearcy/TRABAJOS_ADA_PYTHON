#ejemplo 1: Desempaquetado basico de tuplas
#Crear una tupla con varios tipos de datos

mi_tupla = (1, "Python", 3.14)

#Desempaquetar la tupla en tres variables
numero, lenguaje, pi = mi_tupla

#Mostrar el valor de cada variable despues de desempaquetado
print("Numero:", numero) #Imprime:numero1
print("Lenguaje:", lenguaje) #Imprime Lenguaje: Python
print("Valor de Pi:", pi) # Imprime: Valor de Pi: 3.14

#Explicacion: Aqui, cada valor en la tupla se asigna a una variable correspondiente
#El primer valor de la tupla (1) se asinga a 'numero'
#El segundo valor ("python") se asigna a 'lenguaje'
#El tercer valor(3.14) se asinga a 'pi'

#Ejemplo 2: Numero de variables no coincide con el numero d elementos
#Crear una tupla con tres elementos
mi_tupla = (1,"Python", 3.14)
#intentar desempaquetar en dos vairables(esto causara un error)
#Explicacion: Como hay tres elementos en la tupla, y solo dos variables, Python generara un error.
#La cantidad de variables debe coincidir con la cantidad de elementos en la tupla

#Ejempl 3: Desempaquetando con el operador
#Crear una tupla con varios elementos
mi_tupla = (1, "Python", 3.14, "Tuplas", "Desempaquetado")
#Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto=mi_tupla

#Mostrar los resultados del desempaquetado
print("\nPrimer elemento:", primer_elemento) #Imprime: Primer elemento:1
print("Resto de los elemento:", resto)

#Imrime: Resto de los elementos['Python', 3.14, 'tuplas', 'desempaquetado']
#Explicacion: Aqui, el primer valor de la tupla(1) se asigna  'primer_elemento'
#El resto de los valores se capturan en la lista 'resto' utilizando el operador '*'
#Esto permite manejar un numer variables de elementos en la tupla.
