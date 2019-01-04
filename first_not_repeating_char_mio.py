"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def norepeat(char_sequence):
	letters = ()
	letters_no_repeat = []

	for letter in char_sequence:
		if letters == ():
			letters = (letter,)
			letters_no_repeat.append(letter)
		else:
			in_letters = letter in letters
			if in_letters:
				in_no_repeat = letter in letters_no_repeat
				if in_no_repeat:
					letters_no_repeat.remove(letter)
			else:
				letters = letters + (letter,)
				letters_no_repeat.append(letter)
	if letters_no_repeat != []:
		return letters_no_repeat[0]
	else:
		return "_"

if __name__ == '__main__':
	char_sequence = str(input('Escribe una secuencia de caracteres: '))

	result = norepeat(char_sequence)

	if result == "_":
		print('No hay letras que no se repitan')		
	else:
		print('La primera letra que no se repite es: {}'.format(result))