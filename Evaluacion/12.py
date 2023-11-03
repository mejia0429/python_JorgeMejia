#se utiliza para obtener la longitud o el número de elementos en una secuencia, como una cadena de texto,
#una lista, una tupla o un diccionario

#Ejemplo

frase = input("Ingrese una frase: ")

# Split se utiliza para Dividir la frase en palabras
palabras = frase.split()

# Se utiliza len para contar el número de palabras
numero_de_palabras = len(palabras)

print(f"El número de palabras que hay en la frase es: {numero_de_palabras}")