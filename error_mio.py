# -*- coding: utf-8 -*-

countries = {
	'china': 1380,
	'india': 1331,
	'estados unidos': 325,
	'indonesia': 260,
	'brasil': 207,
	'pakistan': 201,
	'nigeria': 191,
	'blanglades': 162
}


if __name__ == '__main__':
	
	while True:
		country = str(input('Escribe el nombre de un país del que quieras saber su población: ').lower())
		
		try:
			print('La cantidad de habitantes de {}, es de {} millones'.format(country,countries[country]))
			
		except KeyError:
			print('No tenemos la cantidad de habitantes del pais {}'.format(country))			
		else:
			print('¿No te parece genial?')
		finally:
			print('Continúa consultando otros países')