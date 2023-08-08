asignaturas = ["Pensamiento Ingenieril", "Pensamiento Algoritmico", "Algebra Lineal", "Geometria", "Calculo"] 
notas = [1.5, 4.6, 4, 2.5, 3.3]
nota_menor=100
for i in range(0,len(notas),1):
    if notas[i]<nota_menor:
        nota_menor=notas[i]
print(nota_menor)