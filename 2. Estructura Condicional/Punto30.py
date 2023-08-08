#30. Leer tres números enteros y determina si el penúltimo dígito de los tres números es igual.
print("Hola usuario, ingrese 3 números enteros y yo determinaré si el penúltimo digito es igual en los 3 números.")
Numero1=int(input("Ingrese el primer número por favor: "))
Numero2=int(input("Ingrese el segundo número por favor:"))
Numero3=int(input("Ingrese el tercer número por favor: "))

penultimoDigito1=(Numero1//10)%10
penultimoDigito2=(Numero2//10)%10
penultimoDigito3=(Numero3//10)%10

if penultimoDigito1==penultimoDigito2 == penultimoDigito3:
    print("Los tres penúltimos digitos de los números ingresados, son iguales.")
else:
    print("El penúltimo digito de los 3 números que ingresaste son diferentes")
