matriz=[[5,3,2],
[4,6,5],
[8,5,3]]
posicion=0
for i in range(0,len(matriz),1):
    for j in range(0,len(matriz[i]),1):
        if posicion==0 and j==0:
            print(matriz[i][j]) 
            posicion+=1
        if posicion==1 and j==1:
            print(matriz[i][j])
            posicion+=1
        if posicion==2 and j==2:
            print(matriz[i][j])
            posicion+=1
