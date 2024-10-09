#Lista inicial
mi_lista = [10, 20, 30, 40, 50]
print('Lista original:', mi_lista)

#Actualizar un elemento especifico
mi_lista[2] = 35 #se actualiza indice 2, 3er elemento
print('Lista despues de actualizar el tercer elemento:', mi_lista)

#Actualizar un elemento usando indice negativo
mi_lista[-1] = 60 #actualiza el ultimo indice (-1) con valor 50 por 60
print('Lista despues de actualizar el utlimo elemento:', mi_lista)

#Actualizar varios elementos usando slicing.
mi_lista[1:4] = [25, 35, 45] # toma en cuenta los datos entre los elementos (1 y 4) y los modifica en ese orden
print('Lista despues de actualizar un rango de elementos:', mi_lista)

#Actualizar elementos basado en una condicion
for i in range(len(mi_lista)):
    if mi_lista[i] > 30:
        mi_lista[i] += 10
print('lista despues de actualizar elementos mayores que 30:', mi_lista)

