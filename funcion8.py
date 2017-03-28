print "_______________________________________________"
print "Generar un intervalo de n numeros entre 20 y 60"
print "_______________________________________________"

def fun1(n,h):
	while n <= 60:
		if n % 2 == 0:
			h += ' %i ' % n
		n += 1
	return h


a = 20
b = ''

print fun1(a,b)

