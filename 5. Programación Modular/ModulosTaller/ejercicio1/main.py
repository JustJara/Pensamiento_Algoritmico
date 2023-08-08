import FuncionesMenu.creadora_matriz as crearMatriz
import FuncionesMenu.ventasmensuales as ventasMensuales
import FuncionesMenu.montoanual as montoAnual
import FuncionesMenu.mayorventasjulio as ventasJulio
import FuncionesMenu.mayorventadepartamento as mayorventapordep
matriz=crearMatriz.matriz()
print(matriz)
encendido=True
while encendido:
    print("Hola, te acabo de generar una matriz donde encontrarás 5 departamentos con sus respectivas cantidades de ventas en los 12 meses del año.")
    print("Cuéntame qué deseas hacer con esta matriz: ")
    print("Presiona 1, si deseas conocer las ventas mensuales de la fábrica.")
    print("Presiona 2, si deseas conocer el monto anual que genera la fabrica completa.")
    print("Presiona 3, si deseas conocer cuál fue el departamento que más ventas obtuvo en el mes de Julio.")
    print("Presiona 4, si deseas saber cual fue el mes que más vendió un departamnto que tu escojas.")
    respuesta_menu=int(input())
    ventas_mensuales=ventasMensuales.ventas_mensuales_fabrica(matriz)
    montoanual= montoAnual.Monto_anual(ventas_mensuales)
    ventasjulio=ventasJulio.mayor_ventas_julio(matriz)
    if respuesta_menu==1:
        print("Las ventas mensuales de cada departamento son:",ventas_mensuales)
    if respuesta_menu==2:
        print("El monto anual que generó la fábrica fue de: ",montoanual,"COP")
    if respuesta_menu==3:
        print("El departamento que más vendio en el mes de Julio fue: ",ventasjulio)
    if respuesta_menu==4:
        print("Cuál departamento quieres conocer su mes con mayor venta.")
        departamento=int(input())
        print("El departamento numero ",departamento,"tuvo registrado como mayor cantidad de ventas en el mes: ",mayorventapordep.Mayor_venta_x_dep(matriz,departamento))
    print("Espero haber sido de ayuda, recuerda que si necesitas algo puedes solicitarlo con el menú anterior.")
    if respuesta_menu==5:
        print("Hasta luego, vuelva pronto.")
        encendido=False