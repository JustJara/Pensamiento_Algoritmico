def Monto_anual(ventas_mensuales):
    monto_anual=0
    for i in range(0,len(ventas_mensuales),1):
        monto_anual+=ventas_mensuales[i]
    return monto_anual