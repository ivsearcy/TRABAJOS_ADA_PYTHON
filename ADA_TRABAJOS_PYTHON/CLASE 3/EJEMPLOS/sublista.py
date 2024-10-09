mi_lista = ['a', 'b', 'c', 'd', 'e']

#acceso por indice
#cada elemento en una lista tiene un indice asociado,
#comenzando desde 0. Puedes acceder a un elemento
#usando su indice entre corchetes [].
print("primer elemento:", mi_lista[0])
print('Tercer elemento:', mi_lista[2])

#acceso por indice negativo
#los indices negativos permiten acceder a los elementos desde
#el final de la lista. El indice -1 se refiere al 'ultimo elemento,
# -2  al penultimo y asi sucesivamente.

print('ultimo elemento:', mi_lista[-1])
print('penultimo elemento:', mi_lista[-2])

#acceso a sublistas(slicing)
#puedes obtener una sublista utilizando el "slicing"(rebanado)
# con la notacion[inicio:fin]. Esto devuelve una nueva lista que
#contiene los elementos desde el indice incio hasta el indicie fin -1.
print("sublista (indice 1 a 3):", mi_lista[1:4])
print("sublista(indice a 3):", mi_lista[:3])
print("sublista(indice 2 a final):", mi_lista[2:])

#acceso con paso en slicing
#puedes especificar un paso en la notacion de slicing
#esto permite obtener elementos con un intervalo especifico.
print('sublista con paso 2:', mi_lista[::2])
print("sublista con paso 2 en rango(1 a 4):", mi_lista[1:4:2])

#iteracion a traves de una lista
#puedes usar un buclre for para interar sobre todos los elementos de la lista
print("Iteracion a traves de la lista:")
for elemento in mi_lista:
    print(elemento)