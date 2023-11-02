#una excepción es un evento anormal o inusual que ocurre durante la ejecución de un programa y altera 
# el flujo normal de su ejecución. Pueden ocurrir por diversas razones, como errores de sintaxis, 
# operaciones matemáticas inválidas, manipulación de estructuras de datos incorrecta.


#Ejemplo

try:
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    
    resultado = numerador / denominador
    
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Número inválido.")


