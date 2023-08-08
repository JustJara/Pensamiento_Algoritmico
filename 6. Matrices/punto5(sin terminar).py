matriz=[[3,2,9],[50,45,20],[2,26,30]]
for i in range(0,len(matriz),1):
    for j in range(0,len(matriz[i]),1):
        if i==j:
            print(matriz[i][j])