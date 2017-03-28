print "________________________________________________________"
print "                  Calculo de Hipotenusa"
print "________________________________________________________"

import math

def fun1(a,b):
	c=math.sqrt((a*a+b*b))
	return (str(c))




num1=float(input("ingrese un cateto\n"))
num2=float(input("ingrese el otro cateto\n"))

print "El resultado es:"
print fun1(num1,num2)

