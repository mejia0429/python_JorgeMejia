#una variable global se declara en una función utilizando la palabra clave global seguida del nombre 
# de la variable.

#Ejemplo


variable = 5

def modifica():
    global variable  
    variable= 12   
    print("Dentro de la función:", variable)

modifica()
print("Fuera de la función:", variable)
