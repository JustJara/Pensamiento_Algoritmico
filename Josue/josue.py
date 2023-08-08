resultados = [[4, 3], [0, 2], [1, 0], [0, 0],[2, 2], [1, 0], [0, 4], [0, 5],[1, 4], [5, 2], [3, 0], [3, 1],[4, 0], [0, 5], [5, 2], [3, 5],[2, 1], [2, 3], [5, 1]]
puntos=0
victorias=0
empates=0
derrotas=0
goles_favor=0
goles_contra=0
valla_invicta=0
mayor_diff_gol=0
menor_diff_gol=0
for i in range(0,len(resultados),1):
    goles_favor+= resultados[i][0]
    goles_contra+= resultados[i][1]
    for j in range(0,1,1):
        if resultados[i][j+1]==0:
            valla_invicta+=1
        if resultados[i][j]>resultados[i][j+1]:
            puntos+=4
            victorias+=1
            diff_gol_victoria=resultados[i][j]-resultados[i][j+1]
            if diff_gol_victoria>mayor_diff_gol:
                mayor_diff_gol=diff_gol_victoria
                jornada_mayor_diff_gol= i
                marcador_mayor_dif_gol= resultados[i]
        elif resultados[i][j]==resultados[i][j+1]:
            puntos+=1.5
            empates+=1
        elif resultados[i][j]<resultados[i][j+1]:
            puntos+=0
            derrotas+=1
            diff_gol_derrota=resultados[i][j+1]-resultados[i][j]
            if diff_gol_derrota>menor_diff_gol:
                menor_diff_gol=diff_gol_derrota
                jornada_menor_diff_gol= i
                marcador_menor_dif_gol= resultados[i]
prom_goles_favor= goles_favor/len(resultados)
prom_goles_contra= goles_contra/len(resultados)
diferencia_gol= goles_favor-goles_contra
print("- Total de Puntos Obtenidos: ",puntos)
print("- Cantidad de Victorias: ",victorias)
print("- Cantidad de Empates: ",empates)
print("- Cantidad de Derrotas: ",derrotas)
print("- Goles a favor: ", goles_favor)
print("- Goles en contra: ", goles_contra)
print("- Diferencia de gol: ",diferencia_gol)
print("- Promedio de goles anotados: ",prom_goles_favor)
print("- Promedio de goles recibidos: ",prom_goles_contra)
print("- Cantidad de vallas invictas: ",valla_invicta) 
print("- Mayor Victoria en la jornada: ",jornada_mayor_diff_gol+1," Con un marcador de: ",marcador_mayor_dif_gol) 
print("- Peor Derrota en la jornada: ",jornada_menor_diff_gol+1," Con un marcador de: ",marcador_menor_dif_gol) 