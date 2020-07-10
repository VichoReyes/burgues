# -*- coding: utf-8 -*-
# Eso de arriba, prato, es para que el juego pueda tener tildes y eñes sin problemas

from random import randint, shuffle

print """                                                       Bienvenido a 
-----------------------------------------------------------------------------------------------------------------------------------------
'   |||||||    |||                  |||||||||       |||	    |||     |||||||       |||||||||     |||     |||     |||||||     ||||||||    '
'   |||	       |||                  |||	   |||      |||	    |||     |||   |||    |||            |||     |||     |||         |||         '
'   ||||||     |||                  |||||||||       |||	    |||     |||||||     |||   |||||||   |||     |||     ||||||      ||||||||    '
'   |||        |||                  |||    |||       |||   |||      ||| ||       |||     |||    |||     |||     |||              |||    '
'   |||||||    |||||||              |||||||||         |||||||       |||  |||      |||||||||       |||||||       |||||||     ||||||||    '
-----------------------------------------------------------------------------------------------------------------------------------------"""

def contar(barrio, dueno):
	tuyos = -1
	otros = -1
	for x in tablero:
		if x.dueno == dueno and x.barrio == barrio:
			tuyos += 1
		if x.barrio == barrio:
			otros += 1
	if tuyos == otros:
		return 3
	else:
		return tuyos

#una cantidad increíble de clases que le hacen a uno la vida más fácil
#(Las clases son formas propias de hacer variables. Así como se puede por default hacer strings e ints)
class Casilla(object):
	def __init__(self, nombre, precio, pago, barrio, casa1, casa2, casa3, casa4, hotel, costCasa):
		super(Casilla, self).__init__()
		self.barrio = 'pertenece al barrio ' + barrio
		self.nombre = nombre
		self.pago = [pago * 2, casa1, casa2, casa3, casa4, hotel]
		self.precio = precio
		self.costCasa = costCasa
	dueno = 'nadie'
	numCasas = 0
class Railroad(object):
	def __init__(self, nombre):
		super(Railroad, self).__init__()
		self.nombre = 'Estación ' + nombre
	dueno = 'nadie'
	precio = 200
	barrio = 'es una estación de metro'
	numCasas = 0
class Utility(object):
	def __init__(self, nombre):
		super(Utility, self).__init__()
		self.nombre = nombre
	precio = 150
	barrio = 'es una utilidad'
	dueno = 'nadie'
	numCasas = 0
class Comchest(object):
	def __init__(self):
		super(Comchest, self).__init__()
	nombre = 'Community Chest'
	dueno = 'Community Chest'
	barrio = 'nada'
class Tax(object):
	def __init__(self, name, quantity):
		super(Tax, self).__init__()
		self.nombre = name
		self.pago = quantity
	dueno = 'taxman'
	barrio = 'nada'
class Jugador(object):
	def __init__(self, nombre):
		super(Jugador, self).__init__()
		self.nombre = nombre
	boardPlace = 0
	money = 1500
	#Esto es un muy útil raw_input personalizado, incluye todas las funciones extra que puedes hacer en cualquier parte del turno. Es el motor de todas las desiciones
	def pregunta(self, texto, lugar):
		respuesta = 'default'
		while respuesta[0] != 's' and respuesta[0] != 'n' and respuesta[0] != 'a':
			respuesta = raw_input(texto + ' Escribe "opciones" para ver otras cosas que puedes hacer     ').lower()
			while len(respuesta) == 0:
				print 'Por favor escribe algo'
				respuesta = raw_input(texto + '     ').lower()
			if respuesta[0] == 's' or respuesta[0] == 'a' or respuesta[0] == 'n':
				continue
			# Letras ocupadas: s, n, d, h, p, o, c, i, e, t, a y else
			#dinero actual:
			if respuesta[0] == 'd':
				print self.money
			#hipotecar
			elif respuesta[0] == 'h':
				# Ésto te muestra tus propiedades
				print 'Éstas son tus propiedades no hipotecadas:'
				for a in tablero:
					if a.dueno == self and a.numCasas == 0:
						print 'La propiedad %s, en la posición %i del tablero. Recibirías %i por hipotecarla.' %(a.nombre, tablero.index(a), a.precio/2)
				print 'Éstas son tus propiedades hipotecadas:'
				for a in tablero:
					if a.dueno == i and a.numCasas == -1:
						print 'La propiedad %s, en la posición %i del tablero. Deshipotecarla cuesta %i.' %(a.nombre, tablero.index(a), (a.precio/2)*1.1)
				while True:					
					propiedadDeseada = raw_input('Qué propiedad quieres hipotecar/deshipotecar? (Escribe su posición)     ')
					if propiedadDeseada.isdigit():
						propiedadDeseada = int(propiedadDeseada)
						if propiedadDeseada >= 0 and propiedadDeseada <= 39 and tablero[propiedadDeseada].dueno == self:
							if tablero[propiedadDeseada].numCasas == 0:
								self.money += tablero[propiedadDeseada].precio/2
								tablero[propiedadDeseada].numCasas = -1
								print 'Se ha hipotecado tu propiedad.'
								break
							else:
								self.money -= tablero[propiedadDeseada].precio/2 + tablero[propiedadDeseada].precio/10
								tablero[propiedadDeseada].numCasas = 0
								print 'Se ha deshipotecado tu propiedad.'
								break
						else:
							print 'No entendí tu orden. Escribiendo "cancelar" puedes salir de las hipotecas. Por favor escribe la posición de una de tus propiedades'
					elif propiedadDeseada == 'c' or propiedadDeseada == 'cancelar':
						break
					else:
						print 'No entendí tu orden. Escribiendo "cancelar" puedes salir de las hipotecas. Por favor escribe un número'
			elif respuesta[0] == 'o':
				print 'Escribiendo "dinero" puedes ver tu dinero actual, escribiendo "hipotecar", hipotecar o deshipotecar propiedades,escribiendo "casas", comprar'
				print 'o vender casas en tus propiedades, escribiendo "intercambiar", intercambiar posesiones con otros jugadores,escribiendo "posición", ver'
				print 'tu posición en el tablero (desde GO), escribiendo "tarjeta", ver la tarjeta de la casilla actual y escribiendo "exit", acabar el juego'
			elif respuesta[0] == 'c':
				#casas
				casasPosibles = []
				for q in tablero:
					if contar(q.barrio, self) == 3 and q.barrio != 'es una estación de metro' and q.barrio != 'es una utilidad':
						casasPosibles.append(q)
				if len(casasPosibles) == 0:
					print 'No puedes poner casas en ninguna de tus propiedades.'
				else:
					print 'Puedes poner casas en las siguientes propiedades, porque tienes todas las de un barrio.'
					for r in casasPosibles:
						print 'La propiedad %s, que pertenece al barrio %s, que tiene %i casa(s) y cada una cuesta %i. Está en la casilla número %i.' %(r.nombre, r.barrio, r.numCasas, r.costCasa, tablero.index(r))
					while True:					
						propiedadObjetivo = raw_input('Qué propiedad quieres hipotecar/deshipotecar? (Escribe su posición)     ')
						if propiedadObjetivo.isdigit():
							propiedadObjetivo = tablero[int(propiedadObjetivo)]
							if casasPosibles.count(propiedadObjetivo) == 1:
								casasParaConstruir = int(raw_input('Cuántas casas quieres construir? (Escribe un número negativo si quieres demoler una)'))
								propiedadObjetivo.numCasas += casasParaConstruir
								if casasParaConstruir < 0:
									self.money += (propiedadObjetivo.costCasa * casasParaConstruir) / 2
								elif casasParaConstruir > 0:
									self.money -= propiedadObjetivo.costCasa * casasParaConstruir
								break
							else:
								print 'No entendí tu orden. Escribiendo "cancelar" puedes salir de las hipotecas. Por favor escribe la posición de una de las propiedades mencionadas anteriormente.'
						elif propiedadObjetivo == 'c' or propiedadObjetivo == 'cancelar':
							break
						else:
							print 'No entendí tu orden. Escribiendo "cancelar" puedes salir de las hipotecas. Por favor escribe un número'
			elif respuesta[0] == 'i':
				print 'Todavía no están configurados los intercambios'
			elif respuesta[0] == 't':
				print 'Todavía no están configuradas las tarjetas'
			elif respuesta[0] == 'p':
				if self.boardPlace == 0:
					print 'Estás en el banco, en GO'
				elif self.boardPlace == 10:
					print 'Estás en la cárcel, pero de visita'
				elif self.boardPlace == 30:
					print 'Estás en la cárcel, maleante!'
				else:
					print 'Estás en la casilla número %i' %(i.boardPlace)
			elif respuesta[0] == 'e':
				print 'Gracias por jugar'
				print ''
				terminar()
			else:
				print 'No entendí tu orden'
			if lugar == 'rendirse' and self.money > 0:
				break
		else:
			return respuesta[0]
class Card(object):
	def __init__(self, descripcion, tipoDeEfecto, efecto):
		super(Card, self).__init__()
		self.descripcion = descripcion
		self.tipoDeEfecto = tipoDeEfecto
		self.efecto = efecto
	def actuar(self, jugador):
		print self.descripcion
		if self.tipoDeEfecto == 'irA':
			if jugador.boardPlace > self.efecto:
				jugador.money += 200
				print 'Como has dado la vuelta al tablero, has ganado 200 al pasar por GO'
			jugador.boardPlace = self.efecto
		else:
			jugador.money += self.efecto

tablero = []

tablero.append(Tax('GO', 0))
tablero.append(Casilla("Franklin", 60, 2, 'morado', 10, 30, 90, 160, 250, 50))
tablero.append(Comchest())
tablero.append(Casilla("Santa Rosa", 60, 4, 'morado', 20, 60, 180, 320, 450, 50))
tablero.append(Tax("Contribuciones de bienes raíces. Debes pagar 200", 200))
tablero.append(Railroad("San Pablo"))
tablero.append(Casilla("Vicuña Mackenna", 100, 6, 'celeste', 30, 90, 270, 400, 550, 50))
tablero.append(Comchest())
tablero.append(Casilla("San Diego", 100, 6, 'celeste', 30, 90, 270, 400, 550, 50))
tablero.append(Casilla("Dragones de la Reina", 120, 8, 'celeste', 40, 100, 300, 450, 600, 50))
tablero.append(Tax("la cárcel, pero de visita", 0))
tablero.append(Casilla("Paseo Huérfanos", 140, 10, 'violeta', 50, 150, 450, 625, 750, 100))
tablero.append(Utility('Chilectra'))
tablero.append(Casilla("Estado", 140, 10, 'violeta', 50, 150, 450, 625, 750, 100))
tablero.append(Casilla("Paseo Ahumada", 160, 12, 'violeta', 60, 180, 500, 700, 900, 100))
tablero.append(Railroad("Baquedano"))
tablero.append(Casilla("Bellavista", 180, 14, 'naranjo', 70, 200, 550, 700, 900, 100))
tablero.append(Comchest())
tablero.append(Casilla("Salvador", 180, 14, 'naranjo', 70, 200, 550, 700, 900, 100))
tablero.append(Casilla("Seminario", 200, 16, 'naranjo', 80, 220, 600, 800, 1000, 100))
tablero.append(Tax("Parada libre", 0))
tablero.append(Casilla("Pedro Bannen", 220, 18, 'rojo', 90, 250, 700, 875, 1050, 150))
tablero.append(Comchest())
tablero.append(Casilla("Américo Vespucio", 220, 18, 'rojo', 90, 250, 700, 875, 1050, 150))
tablero.append(Casilla("Parque Bustamante", 240, 20, 'rojo', 100, 300, 750, 925, 1100, 150))
tablero.append(Railroad("Tobalaba"))
tablero.append(Casilla("Providencia", 260, 22, 'amarillo', 110, 330, 800, 975, 1150, 150))
tablero.append(Casilla("José Zapiola", 260, 22, 'amarillo', 110, 330, 800, 975, 1150, 150))
tablero.append(Utility('Aguas Andinas'))
tablero.append(Casilla("Aguirre Luco", 280, 24, 'amarillo', 120, 360, 850, 1025, 1200, 150))
tablero.append(Tax("Vete a la cárcel!", 0))
tablero.append(Casilla("Francisco Bilbao", 300, 26, 'verde', 130, 390, 900, 1100, 1275, 200))
tablero.append(Casilla("Pocuro", 300, 26, 'verde', 130, 390, 900, 1100, 1275, 200))
tablero.append(Comchest())
tablero.append(Casilla("San Crescente", 320, 28, 'verde', 150, 450, 1000, 1200, 1400, 200))
tablero.append(Railroad("El Golf"))
tablero.append(Comchest())
tablero.append(Casilla("Vitacura", 350, 35, 'azul', 175, 500, 1100, 1300, 1500, 200))
tablero.append(Tax("Impuesto al lujo. Debes pagar 75", 75))
tablero.append(Casilla("Alonso de Córdova", 400, 50, 'azul', 200, 600, 1400, 1700, 2000, 200))

chanceCards = []

chanceCards.append(Card('Parece que a los policías no les importa que tu narcotráfico sea sin fines de lucro. A la cárcel!', 'irA', 30))
chanceCards.append(Card('El "Peace Dance" casi funcionó, porque se notaba cómo ese policía parpadeaba más de lo normal. De todas maneras fuiste a la cárcel', 'irA', 30))
chanceCards.append(Card('La idea es que te quedes paralizado de la emoción, pero supongo que ya nada puede sorprenderte. Ganas 500 en "Quién quiere ser millonario".', 'másDinero', 500))
chanceCards.append(Card('Ezta frase tiene una falta de ortografía, así que te multaron por escribir mal. 15 menos.', 'másDinero', -15))

communityCards = []

j = []
while True:
	jugadores = raw_input('Cuántos jugadores habrá?     ')
	if jugadores == '2' or jugadores == '3' or jugadores == '4':
		jugadores = int(jugadores) + 1
		break
	else:
		print 'Por favor, inserte un número entre 2 y 4'
for x in xrange(1,jugadores):
	j.append(Jugador(raw_input('Jugador ' + str(x) + ', escribe tu nombre     ')))
print 'Entonces, a jugar!'
print ''
shuffle(j)
while True:
	for i in j:
		print 'Ahora le toca a ' + i.nombre
		while True:
			if i.boardPlace == 30:
				fianza = i.pregunta('Quieres pagar 50 para salir de la cárcel?', 'normal')
				if fianza == 's' or fianza == 'a':
					i.money -= 50
					i.boardPlace = 10
					print 'Has salido de la cárcel!'
			dado1 = randint(1, 6)
			dado2 = randint(1, 6)
			dados = dado1 + dado2
			print 'Te salió %i con los dados. (%i + %i)' %(dados, dado1, dado2)
			if i.boardPlace == 30 and fianza == 'n' and dado1 == dado2:
				i.boardPlace = 10
				print 'Como te han salido dados iguales, has salido de la cárcel'
			elif i.boardPlace == 30:
				print 'Como estás en la cárcel, no has avanzado nada.'
				break
			if i.boardPlace + dados < 40:
				i.boardPlace += dados
			else:
				i.boardPlace += (dados - 40)
				i.money += 200
				print 'Has pasado por GO, por lo que has recibido 200'
			casillaActual = tablero[i.boardPlace]
			if casillaActual.dueno == 'nadie':
				opinion = i.pregunta('Has caído en %s, que cuesta %i, %s y no tiene dueño. Quieres comprarla?' %(casillaActual.nombre, casillaActual.precio, casillaActual.barrio), 'normal')
				if opinion == 's' or opinion == 'a':
					casillaActual.dueno = i
					i.money -= casillaActual.precio
					print 'Has comprado esta propiedad'
				else:
					print 'No has comprado esta propiedad'
			elif casillaActual.dueno == 'Community Chest':
				i.pregunta('Has caído en una casilla de tarjeta. Escribe aceptar para verla.', 'normal')
				chanceCards[randint(0,len(chanceCards)-1)].actuar(i)
			elif casillaActual.dueno == 'taxman':
				i.money -= casillaActual.pago
				i.pregunta('Has caído en ' + casillaActual.nombre + '. Escribe "aceptar".', 'normal')
			else:
				if casillaActual.dueno == i:
					i.pregunta('Has caído en ' + casillaActual.nombre + ', que es una propiedad tuya. Escribe "aceptar".', 'normal')
				elif casillaActual.numCasas == -1:
					i.pregunta('Has caído en ' + casillaActual.nombre + ', que es de ' + (casillaActual.dueno).nombre + ', pero está hipotecada. Escribe "aceptar".', 'normal')
				else:
					iguales = contar(casillaActual.barrio, casillaActual.dueno)
					if casillaActual.barrio == 'es una estación de metro':
						i.money -= 25 * (2 ** iguales)
						(casillaActual.dueno).money += 25 * (2 ** iguales)
						i.pregunta('Has caído en %s, que es de %s, al que le tienes que pagar %i. Escribe "aceptar".' %(casillaActual.nombre, (casillaActual.dueno).nombre, 2 ** iguales * 25), 'normal')
					elif casillaActual.barrio == 'es una utilidad' and iguales == 0:
						i.money -= dados * 4
						(casillaActual.dueno).money += dados * 4
						i.pregunta('Has caído en %s, que es de %s, al que le tienes que pagar %i. Escribe "aceptar".' %(casillaActual.nombre, (casillaActual.dueno).nombre, dados * 4), 'normal')
					elif casillaActual.barrio == 'es una utilidad' and iguales == 3:
						i.money -= dados * 10
						(casillaActual.dueno).money += dados * 10
						i.pregunta('Has caído en %s, que es de %s, al que le tienes que pagar %i. Escribe "aceptar".' %(casillaActual.nombre, (casillaActual.dueno).nombre, dados * 10), 'normal')
					else:
						if iguales == 3:
							i.money -= casillaActual.pago[casillaActual.numCasas]
							(casillaActual.dueno).money += casillaActual.pago[casillaActual.numCasas]
							i.pregunta('Has caído en %s, que es de %s, al que le tienes que pagar %i. Escribe "aceptar".' %(casillaActual.nombre, (casillaActual.dueno).nombre, casillaActual.pago[casillaActual.numCasas]), 'normal')
						else:
							i.money -= casillaActual.pago[0] / 2
							(casillaActual.dueno).money += casillaActual.pago[0] / 2
							i.pregunta('Has caído en %s, que es de %s, al que le tienes que pagar %i. Escribe "aceptar".' %(casillaActual.nombre, (casillaActual.dueno).nombre, casillaActual.pago[0]/2), 'normal')
			while i.money < 0:
				rendirse = i.pregunta('Tienes menos dinero que 0. Qué quieres hacer? Escribe "nada" para rendirte.', 'rendirse')
				if rendirse == 'n':
					print 'Gracias por jugar.'
					for a in tablero:
						if a.dueno == i:
							a.dueno == casillaActual.dueno
					j.remove(i)
					break
			if dado1 != dado2:
				break
			else:
				print 'Dados iguales, tira de nuevo!'
		print ''
		if len(j) == 1:
			print 'Felicitaciones, ' + j[0].nombre + '. Has ganado el juego.'
			print ''
			terminar()
