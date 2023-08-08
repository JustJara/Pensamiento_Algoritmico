asignaturas = ["Pensamiento Ingenieril", "Pensamiento Algoritmico", "Algebra Lineal", "Geometria", "Calculo"] 
notas = [1.5, 4.6, 4, 2.5, 3.3]
suma_notas=0
for i in range(0,len(notas),1):
    suma_notas+=notas[i]

promedio_notas=suma_notas/len(notas)
print(promedio_notas)