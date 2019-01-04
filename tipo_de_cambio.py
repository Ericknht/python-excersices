# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
	usd_to_clp_rate = 688.30

	return usd_to_clp_rate * amount

def run():
	print('CALCULADORA DE DIVISAS')
	print('Convierte dólares a pesos chilenos')
	print('')

	amount = float(input('Ingresa la cantidad de dólares que quieres convertir'))

	result = foreign_exchange_calculator(amount)

	print('${} dólares estadounidesnses son ${} pesos chilenos'.format(amount,result))
	print('')

if __name__ == '__main__':
	run()