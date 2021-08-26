from sympy.interactive import printing
import sympy
from sympy import limit, Symbol, S

indicador=int(input("De qué tipo de función quiere calcular el límite: (1) Polinómica - (2) Racional - (3) Irracional: "))

if indicador == 1:
	printing.init_printing(use_latex='mathjax')
	polinomio=input("Ingrese el polinomio: ")
	sympy.init_printing()
	x = sympy.symbols('x')
	pol = sympy.Poly(polinomio)
	xa=float(input("Ingrese el valor al que quiere que se aproxime x: "))
	resultado1a = limit(polinomio, x, xa)
	print("Cuando su función se aproxima a ",xa," el límite es ",resultado1a)


elif indicador == 2:

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

elif indicador == 3:

	printing.init_printing(use_latex='mathjax')
	raiz = int(input("Ingrese el indice de la raiz: "))
	multraiz = float(input("Ingrese el valor que multiplica a la raiz: "))
	sumraiz = float(input("Ingrese el valor que se suma a la raiz: "))
	potenciaxn = float(input("introduzca el valor al que esta elevado x en el numerador: "))
	multiplyxn = float(input("introduzca el valor que multiplica a las x en el numerador: "))
	sumaxn = float(input("introduzca el valor que se suma a las x en el numerador: "))
	potenciaxd = float(input("introduzca el valor al que esta elevado x en el denominador: "))
	multiplyxd = float(input("introduzca el valor que multiplica a las x en el denominador: "))
	sumaxd = float(input("introduzca el valor que se suma a las x en el denominador: "))
	xc=float(input("introduzca el valor al que quiere que se aproxime x: "))
	x = Symbol('x')

	if multiplyxd == 0 or potenciaxd == 0 and raiz >= 1:
		try:
			funcionc=sumraiz+multraiz*(((xc**potenciaxn)*multiplyxn+sumaxn)/((xc**potenciaxd)*multiplyxd+sumaxd))**(1/raiz)
			print("Cuando su función se aproxima a ",xc," el límite existe y es:", funcionc)
		except:
			print("El límite no es posible calcularlo cuando x se aproxima a ",xc)

		
	
	else: 
		funcionc=sumraiz+multraiz*(((xc**potenciaxn)*multiplyxn+sumaxn)/((xc**potenciaxd)*multiplyxd+sumaxd))**(1/raiz)
		try: 
			resultado1c = limit(funcionc, x, xc+0.00000001)
			resultado2c = limit(funcionc, x, xc-0.00000001)
			if round(resultado1c,7) == round(resultado2c,7):
				print("Cuando la función se aproxima a ",xc,"el límite existe y es: ",round(resultado1c))
			elif round(resultado1c,7) == round(resultado2c,7) and round(resultado1c,7)>100000:
				print("Cuando la función se aproxima a ",xc,"el límite existe y es +infinito")
			elif round(resultado1c,7) == round(resultado2c,7) and round(resultado1c,7)<-100000:
				print("Cuando la función se aproxima a ",xc,"el límite existe y es -infinito")
			elif round(resultado1c,7) != round(resultado2c,7) and round(resultado1c,7)>100000 and round(resultado2c,7)<-100000:
				print("Cuando la función se aproxima a ",xc,"el límite no existe dado que +infinito y -infinito son diferentes")
			elif round(resultado1c,7) != round(resultado2c,7) and round(resultado1c,7)<100000 and round(resultado2c,7)>-100000:
				print("Cuando la función se aproxima a ",xc,"el límite no existe dado que +infinito y -infinito son diferentes")
			else:
				print("Cuando la función se aproxima a ",xc,"el límite no existe dado que",round(resultado1c)," y ",round(resultado2c)," son diferentes")
		except: 
			print("No es posible calcular el limite cuando x vale ",xc)
		



else: 
	print("Error de tipeo, por favor, reinicie el programa")
