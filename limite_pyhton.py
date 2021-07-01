from sympy.interactive import printing
from sympy import limit, Symbol, S

printing.init_printing(use_latex='mathjax')
potenciaxn = float(input("introduzca el valor al que esta elevado x en el numerador: "))
multiplyxn = float(input("introduzca el valor que multiplica a las x en el numerador: "))
sumaxn = float(input("introduzca el valor que se suma a las x en el numerador: "))
potenciaxd = float(input("introduzca el valor al que esta elevado x en el denominador: "))
multiplyxd = float(input("introduzca el valor que multiplica a las x en el denominador: "))
sumaxd = float(input("introduzca el valor que se suma a las x en el denominador: "))
xb=float(input("introduzca el valor al que quiere que se aproxime x: "))
x = Symbol('x')

if multiplyxd == 0 or potenciaxd == 0:
	funcion=((xb**potenciaxn)*multiplyxn+sumaxn)/((xb**potenciaxd)*multiplyxd+sumaxd)
	print("Cuando su función se aproxima a ",xb," el límite existe y es:", funcion)
else:
	funcionb=((x**potenciaxn)*multiplyxn+sumaxn)/((x**potenciaxd)*multiplyxd+sumaxd)
	resultado1 = limit(funcionb, x, xb+0.00000001)
	resultado2 = limit(funcionb, x, xb-0.00000001)
	if round(resultado1,7) == round(resultado2,7):
		print("Cuando la función se aproxima a ",xb,"el límite existe y es: ",round(resultado1))
	elif round(resultado1,7) == round(resultado2,7) and round(resultado1,7)>100000:
		print("Cuando la función se aproxima a ",xb,"el límite existe y es +infinito")
	elif round(resultado1,7) == round(resultado2,7) and round(resultado1,7)<-100000:
		print("Cuando la función se aproxima a ",xb,"el límite existe y es -infinito")
	elif round(resultado1,7) != round(resultado2,7) and round(resultado1,7)>100000 and round(resultado2,7)<-100000:
		print("Cuando la función se aproxima a ",xb,"el límite no existe dado que +infinito y -infinito son diferentes")
	elif round(resultado1,7) != round(resultado2,7) and round(resultado1,7)<100000 and round(resultado2,7)>-100000:
		print("Cuando la función se aproxima a ",xb,"el límite no existe dado que +infinito y -infinito son diferentes")
	else:
		print("Cuando la función se aproxima a ",xb,"el límite no existe dado que",round(resultado1)," y ",round(resultado2)," son diferentes")

