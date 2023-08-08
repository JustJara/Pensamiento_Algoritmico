Algoritmo Convertidor_Minutos_Horas
	Definir minutos, horasfinal, horas, minutosfinal Como Real
	Imprimir "Ingrese su valor en minutos"
	leer minutos
	minutosfinal = minutos % 60
	horasfinal = minutos / 60 
	Imprimir "Son " horasfinal "horas y " minutosfinal " minutos"
FinAlgoritmo
