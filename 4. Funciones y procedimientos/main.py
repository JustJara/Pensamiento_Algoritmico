import libreria.funcion_identificar_primo as opr

x=int(input("Ingrese el valor que quiere identificar si es primo: "))
es_primo= opr.identificar_primo(x)
if es_primo:
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")