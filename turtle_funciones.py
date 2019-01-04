# -*- coding: utf-8 -*-

import turtle

def main():
	window = turtle.Screen()
	erick = turtle.Turtle()

	make_square(erick)
	turtle.mainloop()

def make_square(erick):
	length = int(input('Tamaño del cuadrado: '))
	
	for x in range(4):
		make_line_and_turn(erick, length)

def make_line_and_turn(erick, length):
		erick.forward(length)
		erick.left(90)
		

if __name__ == '__main__':
	main()