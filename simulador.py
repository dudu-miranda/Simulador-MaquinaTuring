#!/usr/bin/python
# -*- encoding:utf-8 -*-


from turing import Machine
from fita import Fita
from instrucao import identificaInstrucao
from copy import deepcopy

class Simulador(object):

	"""docstring for Simulador"""
	def __init__(self, fita=Fita(), maquinas={}, maquinaInicial=0):
		self.fita = fita
		self.maquinas = maquinas
		self.maquinaInicial = maquinaInicial
		self.maquinaAtual = self.maquinaInicial



	def __str__(self):
		string = ''
		for m in self.maquinas:
			string += 'maquina: '+str(m)+str(self.maquinas[m])
		return string



	def montaMaquina(self, nome, estadoInicial):
		if(not nome in self.maquinas):
			if self.maquinaInicial == 0:
				self.maquinaInicial = nome
			#print('nome: '+str(nome)+'    estado inicial: '+str(estadoInicial))
			#print(str(self))
			self.maquinas[nome] = Machine(estadoInicial, nome)



	def montaInstrucao(self, instrucao):
		self.maquinas[self.maquinaAtual].addInstrucao(instrucao)
		


	def monta(self, instrucao):
		if instrucao[0] == 'bloco':
			self.montaMaquina(instrucao[1], instrucao[2])
			self.maquinaAtual = instrucao[1]
		elif len(instrucao) > 2:
			self.montaInstrucao(instrucao)
		elif len(instrucao) == 1:
			self.maquinaAtual = self.maquinaInicial



	def entrada(self, value=0):
		if value == 0:
			#Escritos de boas vindas
			print('\nSimulador da Máquina de Turing ver 1.0\n')
			print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação\n')
			print('Eduardo Miranda & Thales Lima, IFMG, 2018. \n\n')

			print('Forneça a palavra inicial: ', end="")

			word = input('')
			return word
		else:
			#Escritos de boas vindas
			print('\nSimulador da Máquina de Turing ver 1.0\n')
			print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação\n')
			print('Eduardo Miranda & Thales Lima, IFMG, 2018. \n\n')

			print('Palavra inicial: '+str(word))



	def run(self, word=0):
		if word == 0:
			word = self.entrada()

		self.fita.startaFita(word)

		pilhaMaquinas = [self.maquinas[self.maquinaInicial]]

		while(pilhaMaquinas):
			n = len(pilhaMaquinas)
			maquina = pilhaMaquinas[n-1]
			self.maquinaAtual = maquina.run(self.fita)

			if(self.maquinaAtual == 'retorne'):
				pilhaMaquinas.pop()

			elif(self.maquinaAtual == 'pare'):
				return 'pare'

			elif(self.maquinaAtual in self.maquinas):
				pilhaMaquinas.append(self.maquinas[self.maquinaAtual])
				continue
			else:
				print('o bloco ['+str(self.maquinaAtual)+'] nao existe')




