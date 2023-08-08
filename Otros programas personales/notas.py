encendido = True
opcion=0
while encendido:
    print("Selecciona una opción")
    opcion= int(input())
    if opcion==1:
        print("Ingresa las notas que deseas calcular el promedio actual de la materia.")
        nota1=float(input("Ingrese la primera nota del exámen: "))
        porcentajeNota1= float(input("Ingrese el porcentaje del examen (SOLO EL NÚMERO): "))

        nota2=float(input("Ingrese la segunda nota del exámen: "))
        porcentajeNota2= float(input("Ingrese el porcentaje del examen (SOLO EL NÚMERO): "))

        nota3=float(input("Ingrese la tercera nota del exámen: "))
        porcentajeNota3= float(input("Ingrese el porcentaje del examen (SOLO EL NÚMERO): "))

        nota4=float(input("Ingrese la cuarta nota del exámen: "))
        porcentajeNota4= float(input("Ingrese el porcentaje del examen (SOLO EL NÚMERO): "))

        nota5=float(input("Ingrese la quinta nota del exámen: "))
        porcentajeNota5= float(input("Ingrese el porcentaje del examen (SOLO EL NÚMERO): "))

        porcentajeNota1 = porcentajeNota1/100
        porcentajeNota2 = porcentajeNota2/100
        porcentajeNota3 = porcentajeNota3/100
        porcentajeNota4 = porcentajeNota4/100
        porcentajeNota5 = porcentajeNota5/100

        promedioNotas = (nota1*porcentajeNota1)+(nota2*porcentajeNota2)+(nota3*porcentajeNota3)+(nota4*porcentajeNota4)+(nota5*porcentajeNota5)
        print("Su promedio actual de las notas es: ", promedioNotas)
    if opcion==2:
        encendido = False
        print("Un placer haberte ayudado")