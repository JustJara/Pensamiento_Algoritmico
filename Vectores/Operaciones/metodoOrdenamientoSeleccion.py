def ordenar_por_seleccion(lista):
    for i in range (0,len(lista)-1,1):
        minimo = i
        for j in range(i+1,len(lista),1):
            if lista[j] < lista[minimo]:
                minimo=j
        aux = lista[i]
        lista[i]= lista[minimo]
        lista[minimo] = aux

    return lista

def busqueda_secuencial(valor,lista):
    for i in range(0,len(lista),1):
        if valor==lista[i]:
            return True        
    return False

def indice_primera_vez_menor(lista):
    numero_menor=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<numero_menor:
            numero_menor=lista[i]
            posicion_numero_menor= i
    return posicion_numero_menor

def indice_primera_vez_mayor(lista):
    numero_mayor=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>numero_mayor:
            numero_mayor=lista[i]
            posicion_numero_mayor= i
    return posicion_numero_mayor