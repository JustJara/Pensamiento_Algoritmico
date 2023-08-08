asignaturas = ["Pensamiento Ingenieril", "Pensamiento Algoritmico", "Algebra Lineal", "Geometria", "Calculo"] 
notas = [1.5, 4.6, 4, 2.5, 3.3]
for i in range(0,len(notas),1):
    if notas[i]<3.0:
        print(asignaturas[i],notas[i])