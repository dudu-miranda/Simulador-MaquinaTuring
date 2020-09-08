#!/usr/bin/python
# -*- encoding:utf-8 -*-


from fita import Fita
from instrucao import identificaInstrucao
from copy import deepcopy

class Machine(object):

	"""docstring for Machine"""
	def __init__(self, estadoInicial, nome):
		self.instrucoes = {}
		self.nome = nome
		self.estadoInicial = int(estadoInicial)
		self.estadoAtual = self.estadoInicial


	def __str__(self):
		string = ''
		for estOri in self.instrucoes:
			string += '\n\testado de origem: '+str(estOri)+'\n'
			for caractere in self.instrucoes[estOri]:
				string += '\t\tcaractere: '+str(caractere)+'   acao: '+str(self.instrucoes[estOri][caractere])+'\n'

		return string


	def fuleragem(self, fita):
		nomeBloco = ''
		for i in range(0,(20-len(self.nome))):
			nomeBloco += '.'
		nomeBloco += str(self.nome)

		nomeEstado = ''
		for i in range(0,(4-len(str(self.estadoAtual)))):
			nomeEstado += '0'
		nomeEstado += str(self.estadoAtual)

		f = fita.fitaFuleragem()

		string = nomeBloco+'.'+nomeEstado+': '+f
		return string


	def executaInstrucao(self, instrucao, fita):
		n = len(instrucao)
		if(n > 1):
			escreve = instrucao[0]
			movimento = instrucao[1]
			novoEstado = instrucao[2]
			fita.escreveFita(escreve)
			fita.moveCabecote(movimento)

			if(novoEstado == '∗'):
				return self.estadoAtual
			else:
				return novoEstado
		else:
			pass


	def run(self, fita):

		#self.estadoAtual = self.estadoInicial
		#retorno = ''

		while(True):

			if((self.estadoAtual == 'retorne') or (self.estadoAtual == 'pare')):
				if(self.estadoAtual == 'pare'):
					print(str(self.fuleragem(fita)))
				#print('####################### MUDANDO DE BROCOOOOOOOOO ##################')
				aux = self.estadoAtual
				self.estadoAtual = self.estadoInicial
				return aux

			caractere = fita.getCaracter()

			#input('')
			#print('############################################################')
			#print('estado atual: '+str(self.estadoAtual)+'   bloco: '+str(self.nome)+'   estado: '+str(self.estadoAtual)+'   caractere: '+str(caractere)+'\n')
			#print(str(self)+'\n')
			#print('caracteres do estado ('+str(self.estadoAtual)+'): '+str(list(self.instrucoes[self.estadoAtual].keys()))+'\n')
			#print(str(fita)+'\n')

			if(caractere in self.instrucoes[self.estadoAtual]):
				# executa a acao de caractere
				inst = self.instrucoes[self.estadoAtual][caractere]
				#print('caractere: '+str(caractere)+'   instrucao: '+str(inst)+'\n')
				print(str(self.fuleragem(fita)))
				self.estadoAtual = self.executaInstrucao(inst, fita)
				#print(str(fita)+'\n')
			elif('∗' in list(self.instrucoes[self.estadoAtual].keys())):
				# executa a acao de '*'
				inst = self.instrucoes[self.estadoAtual]['∗']
				#print('caractere: ∗   instrucao: '+str(inst)+'\n')
				print(str(self.fuleragem(fita)))
				self.estadoAtual = self.executaInstrucao(inst, fita)
				#print(str(fita)+'\n')
			else:
				# nao achou uma acao
				# ou é um outro bloco ou é um erro
				# retorne o que esta em self.instrucao[self.estadoAtual]
				bloco = list(self.instrucoes[self.estadoAtual].keys())[0]
				if(len(self.instrucoes[self.estadoAtual][bloco]) > 1):
					# erro
					print('o estado ('+str(self.estadoAtual)+') do bloco ['+str(self.nome)+'] não possui ligacao para o caracter {'+str(caractere)+'}')
					return 'pare'
				else:
					# bloco
					#print('bloco: '+str(bloco)+'   estado: '+str(self.instrucoes[self.estadoAtual][bloco])+'\n')
					#print(str(fita)+'\n')
					self.estadoAtual = self.instrucoes[self.estadoAtual][bloco][0]
					return bloco

	def addInstrucao(self, instrucao):
		#instrucao = deepcopy(inst)
		n = len(instrucao)-1
		instrucao[0] = int(instrucao[0])
		if instrucao[n].isdigit():
			instrucao[n] = int(instrucao[n])

		estadoOrigem = instrucao[0]
		caractere = instrucao[1]

		if(not estadoOrigem in self.instrucoes):
			self.instrucoes[estadoOrigem] = {}

		if(n > 3):
			self.instrucoes[instrucao[0]][instrucao[1]] = instrucao[3:]
		else:
			self.instrucoes[instrucao[0]][instrucao[1]] = instrucao[2:]
