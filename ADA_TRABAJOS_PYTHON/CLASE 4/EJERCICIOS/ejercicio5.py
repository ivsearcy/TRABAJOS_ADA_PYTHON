#Ejercicio 5: Manejo de Matrículas en una Tupla
#PASO1. Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
matriculas = (101, 102, 103, 104, 105)

#PASO 2. Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
busqueda1= matriculas.count(102)

#PASO 3. Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.
busqueda2= matriculas.index(104)

print(f"la matricula 102 se encuentra", busqueda1 , "veces")
print(f"La matricula 104 se encuentra en la posicion:", busqueda2)