#Este es un programa para clasificar personas segun su edad 
# utilizando if tradicional con operadores logicos (and, or)

#Defino mis variables
edad=int(input("Ingresa tu edad con numero: ")) #Solicito la edad

if edad <=12: #Niño o niña #Categoria 1 si tiene entre 0 y 12 años es Niño/a
    print('Eres un niño o niña.')
elif (edad ==13 or edad <=19): #adolescente Categoria 2 Si tiene entre 13 y 19 años es Adolescente
    print('Eres un/una adolscente.')
elif (edad ==20 or edad <=64):#adulto si tiene entre 20 y 64 años es Adulto
    print ('Eres un/una Adulto/a.')
else: #adulto mayor Si mas de 65 es Adulto mayor
    print ("Eres adulto mayor. ")

