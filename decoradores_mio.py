# -*- coding: utf-8 -*-

def otra():
	
	print('Ejecutamos la funcion otra')
	
	def interna_otra():
		print('Ejecutamos la funcion interna_otra')
		return 3
	
	return interna_otra
	
def numero():
	return 1

def run():
	funcion_run = 'Soy función run'
	print('Soy imprimir dentro de run, Ejecutamos la función run')
	return funcion_run

if __name__ == '__main__':
	print('------run()--------')
	run()
	print('------run--------')
	print(run)
	print('''
		run()-> Es la ejecución de la función y entrega un retorno, un resultado
		run -> Es la función en sí, el objeto función, su código
		''')
	print('========= run = otra () ================')
	run = otra()
	print('------run()--------')
	run()
	print('------run--------')
	print(run)
	print('-----otra()---------')
	otra()
	print('-----otra---------')
	print(otra)
	print('''
		Al asignar run = otra() ,
		Se ejecuta otra(), por lo que ejecuta su código interno y el resultado (que en este caso es una funcion [interna_otra]) es almacenada en run.
		Como run es otra función, se le puede asignar otra funcion

		Por lo tanto, al ejecutar:
		run() -> Ejecutra la función run(), que en este caso ahora es la funcion interna_otra, por lo que en realidad se está ejecutando interna_otra()
				Lo que da como muestra: Ejecutamos la funcion interna_otra y retorna 3, que en este caso no es alamcenado ni impreso
		
		run -> Es la función interna_otra en sí

		otra() -> Ejecuta la función otra(), por lo que imprime: Ejecutamos la función otra, y retorna la función interna_otra, que en este caso no es alamcenado ni ejecutado

		otra -> Es la función otra en sí, el objeto función

		
		''')
	print('======== run = otra =================')
	run = otra
	print('-----otra()---------')
	otra()
	print('------run()--------')
	run()
	print('------run--------')
	print(run)
	print('------otra--------')
	print(otra)
	print('''
			Al asignar run = otra
			Asignamos la función otra a run, como las dos son funciones run ahora es igual a otra
			
			otra() -> Ejecuta la función otra(), por lo que imprime: Ejecutamos la función otra, y retorna la función interna_otra, que en este caso no es alamcenado ni ejecutado
			
			run() -> como run = otra, Ejecuta la función otra(), por lo que imprime: Ejecutamos la función otra
			
			run -> como run = otra, Es la función otra en sí

			otra -> Es la función otra en sí, el objeto función
		''')

	