def identificar_primo(x):
    contador_primo= 0
    for i in range (1,x+1,1):
        if x%i==0:
            contador_primo+= 1
    return contador_primo==2
