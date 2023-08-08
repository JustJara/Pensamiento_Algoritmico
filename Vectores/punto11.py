""""Escribir un programa que pregunte al usuario los números ganadores de la lotería, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""
lista=[]

n1=int(input("Ingrese el número ganador de la lotería: "))
lista.append(n1)
n2=int(input("Ingrese el número ganador de la lotería: "))
lista.append(n2)
n3=int(input("Ingrese el número ganador de la lotería: "))
lista.append(n3)
n4=int(input("Ingrese el número ganador de la lotería: "))
lista.append(n4)
print(lista)
import Operaciones.metodoOrdenamientoSeleccion as seleccion
print(seleccion.ordenar_por_seleccion(lista))