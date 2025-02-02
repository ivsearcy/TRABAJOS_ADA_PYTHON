#Crear conjunto
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
conjunto_c = {7, 8, 9}

#Subconjunto
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(f"Es conjunot_a un subconjunto de conjunto_b: {es_subconjunto}")

#Superconjunto
es_superconjunto = conjunto_b.issuperset(conjunto_a)
print(f"Es conjunto_b un superconjunto de conjunto_a?: {es_superconjunto}")

#Disconjuntos
son_disconjuntos = conjunto_a.isdisjoint(conjunto_c)
print(f"Diferencia simetrica entre conjunto_a y conjunto_b: {son_disconjuntos}")

#Simetria
simetria = conjunto_a.symmetric_difference(conjunto_b)

print(f"Diferencia simetrica entre conjunto_a y conjunto_b: {simetria}")



#Union update
conjunto_a.update(conjunto_b)
print(f"Conjunto_a despues de la union conjunto_b: {conjunto_a}")

#Interseccion update
conjunto_a.intersection_update(conjunto_b)
print(f"Conjunto_a despues de la union con conjunto_b: {conjunto_a}")

#Difference update
conjunto_a.difference_update(conjunto_b)
print(f"Conjunto_b despues de la diferencia con conjunto_c: {conjunto_a}")

#Symmetric Difference update
conjunto_a.symmetric_difference_update(conjunto_b)
print(f"Conjunto_b despues de la diferencia simetrica con conjunt_b: {conjunto_b}")


