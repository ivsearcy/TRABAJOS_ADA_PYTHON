#Este es un programa que asignara al valor de una calificacion si es aprobado o reprobado.


#Debo solicitar el ingreso de la calificacion entre 0 y 100
calificacion = int(input('Tu calificación debe ser ingresada a continuación, recuerda utilizar el valor de 0 a 100:'))

#Una vez recibida la calificación el programa imprimira si es aprobado o reprobado
# si es mayor o igual a 60 sera aprobado y si es menor a 60 sera reprobado
if calificacion>= 60:
    print("Tu calificación ha sido aprobada")
elif calificacion < 60:
    print("Tu calificación ha sido reprobada")