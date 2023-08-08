#test de separacion de digitos


numero= int(input("Ingrese el numero: "))
123456
primerDigito= numero//100000
segundoDigito= (numero//10000)%10
tercerDigito= (numero//1000)%10
cuartoDigito= (numero//100)%10
quintoDigito= (numero//10)%10
sextoDigito= numero%10

print(primerDigito, segundoDigito, tercerDigito, cuartoDigito, quintoDigito, sextoDigito)
