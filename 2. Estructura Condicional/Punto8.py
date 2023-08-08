# 8. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.
print("Hola usuario, si me das 2 numero enteros de dos digitos te diré si tienen un digito en común")
Numero1 = int(input("Ingresa el primer número por favor: "))
Numero2 = int(input("Ingresa el segundo número por favor: "))
if Numero1<=9 or Numero1>=100 or Numero2<=9 or Numero2>=100:
    print("Ingrese números válidos, que solo contengan 2 DIGITOS.")
else:
    primerDigito1=int(Numero1//10)
    segundoDigito1=int(Numero1%10)
    primerDigito2=int(Numero2//10)
    segundoDigito2=int(Numero2%10)
if primerDigito1==primerDigito2 and segundoDigito1==segundoDigito2:
    print("Ambos números tienen los dos digitos en común.")
else:
    if primerDigito1==primerDigito2:
        print("El número 1 y el número 2 tiene en común el primer digito")
    if primerDigito1==segundoDigito2:
        print("El número 1 tiene en comun el primer digito con el segundo digito del otro número")
    if segundoDigito1==segundoDigito2:
        print("El número 1 y el número 2 tiene en común el primer digito")
    if segundoDigito1==primerDigito2:
        print("El primer número tiene en común el segundo digito con el primer digito del otro número")

    
    