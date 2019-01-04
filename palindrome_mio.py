# -*- coding: utf-8 -*-

def run(word):
	palindrome = word[::-1]
	if palindrome == word:
		return True
	return False

if __name__ == '__main__':
	print('En este programa puedes ingresar una palabra y ver si es un palíndromo')
	word = str(input('Ingresa una plabra: '))
	result = run(word)
	if result:
		print('Tu palabra "{}" es un palíndromo'.format(word))
	else:
		print('Tu palabra "{}" NO es un palíndromo'.format(word))
