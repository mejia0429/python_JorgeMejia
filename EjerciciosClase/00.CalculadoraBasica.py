#Crea un programa que actúe como una calculadora básica. Pide al usuario dos números y luego permite al
#usuario elegir una operación (suma, resta, multiplicación, división). Muestra el resultado en pantalla.

#seleccion = 0
num1 = float(input ("Por favor ingrese el primer numero: "))
num2 = float(input ("Por favor ingrese el segundo numero: "))
#suma= num1+num2
#resta= (num1-num2)
#multiplicacion= (num1*num2)
#division= (num1/num2)

print("")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DIVISION")
print("")

print("")
eleccion = input("Digite la opción deseada para realizar la operación: ")

if eleccion == "1":
    resultado = num1 + num2
elif eleccion =="2":
    resultado = num1 - num2
elif eleccion =="3":
    resultado = num1 * num2
elif eleccion =="4":
    resultado = num1 / num2
    
else:
    resultado = ("Operación no válida")
    
print("El resultado es: " +str(resultado))
