# -*- coding: utf-8 -*-
import random

def run(less, higher):
	number_found = False
	random_number = random.randint(less,higher)

	while not number_found:
		number = int(input('Intenta un número entre {} y {} : '.format(less,higher)))

		if number == random_number:
			print('Felicidades, encontráste el número')
			number_found = True
		elif number > random_number:
			print('El número es más pequeño')
		else:
			print('El número es más grande')


if __name__ == '__main__':
	print("Crea un intervalo, yo el gran Erick Machine, elegiré un número y tu tendrás que adivinarlo :P")
	less = int(input('Ingresa el número más pequeño del intervalo: '))
	higher = int(input('Ingresa el número más grande del intervalo: '))
	run(less, higher)
