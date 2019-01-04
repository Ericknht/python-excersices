# -*- coding: utf-8 -*-

def search_in_list(list_binary, number):

	fin = len(list_binary)
	print(fin)
	middle = len(list_binary)//2
	start = 0

	while True:
		if list_binary[middle] == number:
			print('si está el número {}'.format(number))
			break
		elif list_binary[middle] < number:
			start = middle
			middle = (fin - start)//2 + start
		else:
			fin = middle
			middle = (fin - start)//2 + start
		
		if fin-start == 1:
			print('Este número no está loquillo')
			break


def run():
	list_binary = [3,5,6,3,2,34,54,6,36,7,2,44,69,3,8,3,56,23,6,54]
	search_number = int(input('Ingresa un número para buscarlo en la lista: '))
	
	list_binary.sort()
	print(list_binary)
	search_in_list(list_binary, search_number)
	


if __name__ == '__main__':
	run()