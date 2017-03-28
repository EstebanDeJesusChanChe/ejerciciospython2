print "______________________________________________"
print "              MEDIA DE 3 NUMEROS             "
print" _____________________________________________"


def funcion1 (a,b,c):
	resultado = (a + b + c) / 3
	return (resultado)






#	PROGRAMA PRINCIPAL
num1=float(raw_input("Ingresa un Numero "))
num2 = float(raw_input("Ingresa otro Numero "))
num3 = float(raw_input("Ingresa uno mas "))

#MANDANDO A LLAMAR LA FUNCION
print "EL RESULTADO ES:"
print funcion1(num1,num2,num3)