import random
import string

def generar_contrasena(num_mayusculas, num_minusculas, num_especiales, longitud):
    caracteres = string.ascii_uppercase * num_mayusculas + string.ascii_lowercase * num_minusculas + string.punctuation * num_especiales
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Solicitar entrada del usuario
num_mayusculas = int(input("Ingrese el número de letras mayúsculas: "))
num_minusculas = int(input("Ingrese el número de letras minúsculas: "))
num_especiales = int(input("Ingrese el número de caracteres especiales: "))
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Generar y mostrar la contraseña
nueva_contrasena = generar_contrasena(num_mayusculas, num_minusculas, num_especiales, longitud)
print("Contraseña generada:", nueva_contrasena)