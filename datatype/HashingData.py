#!/usr/bin/python
class HashingData:
	def __init__(self, hora, fichero, hashing):
		self.__hora = hora
		self.__fichero = fichero
		self.__hashing = hashing

	def __str__(self):
		mensaje = "[" + str(self.__hora) + "] " + self.__hashing + " : " + self.__fichero.encode("utf-8") + "\n"
		return mensaje

	__repr__ = __str__