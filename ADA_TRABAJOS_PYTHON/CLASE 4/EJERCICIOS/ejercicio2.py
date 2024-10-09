#Ejercicio 2: Verificación de Elementos en una Tupla
# PASO 1. Crea una tupla llamada mi_tupla con los siguientes elementos: (3, 6, 9, 12, 15).
mi_tupla=(3, 6, 9, 12, 15)

# PASO 2. Verifica si el número 6 está en la tupla y muestra un mensaje indicando si está presente o no.
numero = 6

if numero in mi_tupla:
    print(f"el {numero} si se encuentra presente en la tupla.")


# PASO 3. Verifica si el número 7 está en la tupla y muestra un mensaje indicando si está presente o no.
segundo_numero = 7

if segundo_numero in mi_tupla:
    print(f"el número {segundo_numero} se encuentra present en la tupla")
else:
    print(f"El numero {segundo_numero} no se encuentra presente en la tupla")