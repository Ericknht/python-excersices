# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

words = ['casa',
        'perro',
        'caballo',
        'estufa',
        'secadora',
        'scooter',
        'cepillo',
        'lapiz'
        ]

lines_word = []

word_united = ''



def print_ahorcado(the_index):
    print(IMAGES[the_index])

def select_word():
    random_index = random.randint(0,len(words)-1)
    return words[random_index]

def create_base_word(word):
    for lines in range(len(word)):
        lines_word.append('_')

def input_letter(ahorcado_index):
    letter = str(input('Ingresa una letra: '))
    count = 0
    lost = True
    for letter_word in word:
        if letter == letter_word:
            lines_word[count] = letter
            lost = False
        count += 1

    
    word_united = ''.join(lines_word)
    
    if lost == True:
        ahorcado_index += 1
        print_ahorcado(ahorcado_index)
    else:
        print_ahorcado(ahorcado_index)


    print(word_united)
    
    if ahorcado_index == 7:
        print('Haz perdido, no encontraste la palabra')
        return False, ahorcado_index
    elif word == word_united:
        print('Felicidades encontraste la palabra')
        return False, ahorcado_index
    else:
        return True, ahorcado_index

if __name__ == '__main__':
    print('Bienvenido al juego del ahoracado')
    ahorcado_idx = 0

    print_ahorcado(0)
    word = select_word()

    create_base_word(word)
    
    word_united = ''.join(lines_word)
    print(word_united)

    continue_again = True
    while continue_again:
        continue_again, ahorcado_idx = input_letter(ahorcado_idx)

