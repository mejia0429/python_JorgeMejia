# Escribe un programa que cuente el número de palabras en una frase ingresada por el usuario. 
# Una palabra se define como cualquier secuencia de caracteres separados por espacio.


frase = input("Ingrese una frase: ")

# Split se utiliza para Dividir la frase en palabras
palabras = frase.split()

# Se utiliza len para contar el número de palabras
numero_de_palabras = len(palabras)

print(f"El número de palabras que hay en la frase es: {numero_de_palabras}")