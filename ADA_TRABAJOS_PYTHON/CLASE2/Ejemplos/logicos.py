#definimos distintas variables para usar en las comparaciones
a = 10
b = 5
c = 15
d = 8

#operador AND
#ambas condiciones deben ser verdaderas para que el resultado
resultado_and = (a > b) and (c > d)
print(f"Resultado de (a > b) and (c > d): {resultado_and}")
# (a > b) es true por que 10 > 5
# (c > d) es tru por que 15 > 8
#True and true resulta en true

#operador OR
#Al menos una de las condiciones debe ser verdadera para que el resultado sea True
resultado_or = (a < b) or (c > d) 
print(f"Resultado de (a<b) or (c>d): {resultado_or}" )
#(a<b) es false por que 10 no es menro que 5
# (c>d) es true por que 15>8
#False or true resulta en true

#usamos el operador 'not'
#El operador 'not' invierte el valor de la expresion
resultado_not = not (a<b)
print(f"Resultado de not (a<b): {resultado_not}")
# (a<b) es false por que 10 no es menor que 5
#not false resulta en true

#combinamos los operadores logicos 'and', 'or', 'not' en una sola expresion
resultado_combinado = (a>b) and (not (c<d)) or (b<d)
print(f"Resultado combinado: {resultado_combinado}")
#(a>b) es true por que 10>5
#(c<d) es false por que 15 no es menor que 8, y not(false) resulta en True
#(a>b) and (not(c<d)) es True because true an true resulta en true
#(b<d) es Tru por que 5<8
#True or True resulta en true
