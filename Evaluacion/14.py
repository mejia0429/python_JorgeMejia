#un diccionario es una estructura de datos que permite almacenar pares clave-valor. 
#Cada elemento en un diccionario está asociado con una clave única, y este par clave-valor permite
#la rápida recuperación del valor asociado a través de su clave correspondiente.

#Ejemplo

fruta_color = {
    "Manzana": "Roja",
    "Banano": "Amarillo",
    "Naranja": "Naranja",
    "Pera": "Verde",
    "Uva": "Morada"
    
}

# Accediendo al color de una fruta específica
fruta = "Banano"
print(f"El color de {fruta} es {fruta_color[fruta]}")  


# Iterarando sobre el diccionario 
for fruta, color in fruta_color.items():
    print(f"Fruta: {fruta}, Color: {color}")
