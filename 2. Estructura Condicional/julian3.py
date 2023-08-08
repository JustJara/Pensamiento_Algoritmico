
#diseñe un programa que lea la cantidad de alummnos de redes, contabilidad y diseño y determine el porcentaje 
#de los alumnos de cada uno de los cursos
alumnosRedes = int(input("ingrese la cantidad de alumnosRedes "))
alumnosContabilidad = int(input("ingrese la cantidad de alumnosContabilidad "))
alumnosDiseño = int(input("ingrese la cantidad de alumnosDiseño "))
cienporciento = alumnosContabilidad+alumnosDiseño+alumnosRedes
porcentajeRedes = alumnosRedes*100
porcentajeContabilidad = alumnosContabilidad*100
porcentajeDiseño = alumnosDiseño*100
print("el porcentaje de alummno de redes: ", porcentajeRedes)
print("el porcentaje de alumnos de Diseño: ", porcentajeDiseño)
print("el porcentaje de alumnos de Contabilidad: ", porcentajeContabilidad)
