#Lista inicial
mi_lista = ['a', 'b', 'c', 'd', 'e']

#obtener una sublista del indice 1 al 4 (exlusivo)
sublista1 = mi_lista[1:4] #['b', 'c', 'd,]

#obtener una sublistas desde el inicio hasta el indice 3 (exclusivo)
sublista2= mi_lista[:3] #['a', 'b','c']

#obtener una sublista desde el indice 2 hasta el final
sublista3= mi_lista[2:] #['c','d', 'e']

#obtener una sublista con un paso de 2
sublista4 = mi_lista[::2]

#sublista vacia(si el indice de inicio es mayor que el indice de fin)
sublista_vacia = mi_lista[4:2]


print ("sublista(indice a 4):", sublista1)
print ("sublista (inicio a 3):", sublista2)
print ("sublista indice a final:", sublista3)
print('Sublista con paso 2:', sublista4)
print ("sublista vacia(indice 4 a 2):", sublista_vacia)
