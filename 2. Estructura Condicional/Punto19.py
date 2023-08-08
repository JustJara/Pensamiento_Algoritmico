#Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.
print("Hola usuario, ingrese un número entero de 4 digitos y determinaré cuántos digitos pares tiene.")
Numero=int(input("Ingresa el número por favor: "))
if Numero<=999 or Numero>=10000:
    print("El número ingresado no cumple con las condiciones especificadas.")
else:
    primerDigito=Numero//1000
    segundoDigito=(Numero//100)%10
    tercerDigito=(Numero//10)%10
    cuartoDigito=Numero%10

    if primerDigito%2==0:
        print("El primer digito es par")
    if segundoDigito%2==0:
        print("El segundo digito es par")
    if tercerDigito%2==0:
        print("El tercer digito es par") 
    if cuartoDigito%2==0:
        print("El cuarto digito es par")    
    if primerDigito%2!=0 and segundoDigito%2!=0 and tercerDigito%2!=0 and cuartoDigito%2!=0:
        print("Ninguno de los digitos son pares")