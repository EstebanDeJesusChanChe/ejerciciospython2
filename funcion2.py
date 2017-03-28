import math
print "___________________________________________"
print "          Volumen de una esfera           "
print "___________________________________________"



def funcion1(radio):
	resultado = (4*(math.pi)*(radio*radio*radio))/3
	return (resultado)



#PROGRAMA PRINCIPAL
num1=float(raw_input("Ingresa la Radio del Circulo: "))

#LLAMADA A LA FUNCION

print 'El volumen de la esfera es.'
print funcion1(num1)

