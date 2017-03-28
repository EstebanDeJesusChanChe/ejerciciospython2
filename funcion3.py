print "______________________________________________"
print "     INTERCALACION DE NUMEROS IMPARES          "
print" _____________________________________________"


def funcion1(num):
	for num in range(13, 32):
		if num % 2 != 0:
			print (num)
	
	return num


num1=int(raw_input("Ingresa un 1"))

print funcion1(num1)



#for num in range(13, 32):
#	if num % 2 != 0:
#		print (num)