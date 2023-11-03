import random
import string

def generar_contrasena():
    num_mayusculas = int(input("Ingrese el número de letras mayúsculas: "))
    num_minusculas = int(input("Ingrese el número de letras minúsculas: "))
    num_caracteres_especiales = int(input("Ingrese el número de caracteres especiales: "))
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    
    letras_mayusculas = ''.join(random.choice(string.ascii_uppercase) for _ in range(num_mayusculas))
    letras_minusculas = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_minusculas))
    caracteres_especiales = ''.join(random.choice(string.punctuation) for _ in range(num_caracteres_especiales))
    letras_numeros = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud - num_mayusculas - num_minusculas - num_caracteres_especiales))
    
    contrasena = letras_mayusculas + letras_minusculas + caracteres_especiales + letras_numeros
    contrasena = ''.join(random.sample(contrasena, len(contrasena)))  # Mezclar la contraseña para mayor seguridad
    return contrasena

nueva_contrasena = generar_contrasena()
print("Contraseña generada es:", nueva_contrasena)
