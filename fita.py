#!/usr/bin/python
# -*- encoding:utf-8 -*-

class Fita(object):

	"""docstring for Fita"""
	def __init__(self):
		self.trecho1 = []
		self.trecho2 = []
		self.cabecote = 0
		self.delA = '('
		self.delF = ')'


	def __str__(self):
		return ('trecho2:'+str(self.trecho2)+'   trecho1: '+str(self.trecho1)+'\nfita: '+str(self.getFita())+'   cabecote: '+str(self.cabecote))+'   caracter: '+str(self.getCaracter())


	def fitaFuleragem(self):
		string = ''
		c = self.cabecote
		self.cabecote = self.cabecote - 20
		for i in range(0,41):
			ch = self.getCaracter()
			if(self.cabecote == c):
				string += self.delA+ch+self.delF
			else:
				string += ch
			self.moveCabecote('d')
		self.cabecote = c
		return string



	def startaFita(self, word):
		if(word == ''):
			self.trecho1 = ['_']
		else:
			self.trecho1 = list(word)
		self.cabecote = 0


	#Função que move o cabeçote
	def moveCabecote(self,move):
		if(move == 'i'):
			pass
		elif(move == 'd'):
			self.cabecote = self.cabecote + 1
			if(self.cabecote > (len(self.trecho1)-1)):
				self.trecho1.append('_')
		elif(move == 'e'):
			self.cabecote = self.cabecote - 1
			if(self.cabecote < 0):
				if((abs(self.cabecote)-1) > (len(self.trecho2)-1)):
					self.trecho2.append('_')


	def getCaracter(self):
		#print('cabecote: '+str(self.cabecote)+'   len(trecho1): '+str(len(self.trecho1))+'   len(trecho2): '+str(len(self.trecho2)))

		if(self.cabecote >= 0):
			if((self.cabecote) > (len(self.trecho1)-1)):
				return '_'
			else:
				return self.trecho1[self.cabecote]
		else:
			if((abs(self.cabecote)-1) > (len(self.trecho2)-1)):
				return '_'
			else:
				return self.trecho2[abs(self.cabecote)-1]


	def escreveFita(self,caracter):
		if(caracter == '∗'):
			caracter = self.getCaracter()
		if(self.cabecote >= 0):
			self.trecho1[self.cabecote] = caracter
		else:
			self.trecho2[abs(self.cabecote)-1] = caracter
			

	def getFita(self):
		aux = ''.join(self.trecho2)
		string = aux[::-1]
		string += ''.join(self.trecho1)
		return string
