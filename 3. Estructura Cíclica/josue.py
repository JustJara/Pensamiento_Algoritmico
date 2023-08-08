total_pagar = 0
total_descontado = 0
n_discos = int(input("Ingrese el número de discos que va a comprar: "))

for i in range(0,n_discos,1):
 
    genero = input("Cual es el género del disco: ")
    lanzamiento = int(input("Cual es el año de lanzamiento del disco: "))
    precio = float(input("Cual es el precio del disco: "))
    descuento = 0
    if genero == "Rock" or "rock" and lanzamiento <= 1969:
        descuento = 0.1
    elif genero == "Heavy Metal" and lanzamiento <= 1989:
        descuento = 0.15
    elif genero == "Metal" and lanzamiento <= 1980:
        descuento = 0.15
    elif genero == "Pop" or "pop" and lanzamiento >= 2000:
        descuento = 0.1
    elif genero == "Punk" or "punk" and lanzamiento >= 2000:
        descuento = 0.15
    elif genero == "Salsa" or "salsa" and lanzamiento >= 2005:
        descuento = 0.15

    elif genero == "Disco" or "disco" and lanzamiento <= 1960:
        descuento = 0.25

    precio_con_descuento = precio * (1 - descuento)
    total_pagar = total_pagar + precio_con_descuento
    total_descontado = total_descontado + precio * descuento
print("el total a pagar es:", total_pagar ) 
print("el descuento aplicado fue de:", total_descontado )