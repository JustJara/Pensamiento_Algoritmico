notas=0
cant_alumn=0
cant_alumn= int(input("Ingrese la cantidad de alumnos que presentaron el examen"))
for i in range (1,cant_alumn):
    sum_notas=0
    notas= float(input("ingrese la nota del estudiante", i))
    sum_notas+= i
    prom= sum_notas/cant_alumn
    print ("el promedio de la nota de los estudiantes fue de", prom)
    
