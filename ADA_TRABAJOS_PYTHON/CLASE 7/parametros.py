#Definciion de una funcion que utiliza parametros posicionales, con nombre y predeterminados
def presentar_persona(nombre, edad, ciudad="desconocida", profesion="Desconocida"):

    """
    Presenta informacion sobre una persona.
    
    Parametros: 
    - nombre: (str) Nombre de la presentar_persona.
    - edad: (int) Edad de la persona.
    - ciudad: (str) Ciudad donde vive la persona(opcional).
    - profesion: (str) Profesion de la persona (opcional).
    """
        
print(f"Nombre: {nombre}") 
print(f"Edad: {edad}")
print("Ciudad: {ciudad}")
print(f"profesion: {profesion}")
print()       