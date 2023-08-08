asignaturas = ["Pensamiento Ingenieril", "Pensamiento Algoritmico", "Algebra Lineal", "Geometria", "Calculo"] 
notas = [1.5, 4.6, 4, 2.5, 3.3]
for i in range (0,len(notas)-1,1):
        minimo = i
        for j in range(i+1,len(notas),1):
            if notas[j] < notas[minimo]:
                minimo=j
        aux = notas[i]
        notas[i]= notas[minimo]
        notas[minimo] = aux
        aux1= asignaturas[i]
        asignaturas[i]=asignaturas[minimo]
        asignaturas[minimo]=aux1
print(notas)
print(asignaturas)
