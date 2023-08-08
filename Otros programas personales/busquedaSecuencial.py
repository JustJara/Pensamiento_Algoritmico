def busqueda_secuencial(valor,lista):
    for i in range(0,len(lista),1):
        if valor==lista[i]:
            return True        
    return False
        
valor= int(input("Ingrese el valor a buscar dentro de la lista: "))
lista1=[5,4,9,3,2,6]
resultado= busqueda_secuencial(valor,lista1)
if resultado:
    print("El valor que ingresaste para buscar SI se encuentra en la lista.")
else:
    print("EL valor que ingresaste para buscar NO se encuentra en la lista.")
