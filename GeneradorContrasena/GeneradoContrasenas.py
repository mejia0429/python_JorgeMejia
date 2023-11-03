import random
import string

def generar_contrasena(numMayusculas, numMinusculas, numCaracter, longitud):
    caracteres = string.ascii_uppercase * numMayusculas + string.ascii_lowercase * numMinusculas + string.punctuation * numCaracter
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

while True:
    try:
        numMayusculas = int(input("Ingrese el número de letras mayúsculas: "))
        numMinusculas = int(input("Ingrese el número de letras minúsculas: "))
        numCaracter = int(input("Ingrese el número de caracteres especiales: "))
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        
        if numMayusculas + numMinusculas + numCaracter <= longitud:
            nueva_contrasena = generar_contrasena(numMayusculas, numMinusculas, numCaracter, longitud)
            print("Contraseña generada:", nueva_contrasena)
            break
        else:
            print("Error: La suma de las letras y caracteres colicitados no puede ser mayor que la longitud de la contraseña.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
