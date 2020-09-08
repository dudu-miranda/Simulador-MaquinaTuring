#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy
from instrucao import identificaAcao


class MTuring(object):

	"""Classe que contém a representação de uma máquina de turing que rodará outras máquinas de turing 'menores' """
	def __init__(self, blocos, delA = '(', delF = ')'):
		super(MTuring, self).__init__()
		self.delA = delA
		self.delF = delF
		self.blocos = blocos
		self.pilha = []
		self.fita1 = []
		self.fita2 = []
		self.cabecote = 0	

	#Função que move o cabeçote
	def moveCabecote(self,move):
		if(move == 'i'):
			pass
		elif(move == 'r'):
			self.cabecote +=1
			if(self.cabecote > (len(self.fita1)-1)):
				self.fita1.append('')
		elif(move == 'l'):
			self.cabecote -=1
			if(abs(self.cabecote) > (len(self.fita2)-1)):
				self.fita2.append('')


	def getCaracter(self):
		#print('cabecote: '+str(self.cabecote)+'   len(fita1): '+str(len(self.fita1))+'   len(fita2): '+str(len(self.fita2)))

		if(self.cabecote >= 0):
			if(self.fita1[self.cabecote] == ''):
				return '_'
			else:
				return self.fita1[self.cabecote]
		else:
			if(self.fita2[abs(self.cabecote)-1] == ''):
				return '_'
			else:
				return self.fita2[abs(self.cabecote)-1]



	#Função que acha o id de um bloco a partir de seu nome
	def achaId(self,nomeBloco):
		for block in self.pilha:
			if(block.nomeBloco == nomeBloco):
				return block.idBloco
		return False


	def fuleragem(self, bloco):
		n = 16 - len(bloco.nomeBloco)
		string = '\n'
		for x in range(0,n):
			string += '.'
		string += bloco.nomeBloco+'.'

		estado = str(bloco.estadoAtual)
		n = 4 - len(estado)
		for x in range(0,n):
			string += '0'
		string += str(estado)
		
		c = self.cabecote
		for i in range(0,20):
			self.moveCabecote('l')
		for i in range(0,40):
			if(self.cabecote == c):
				string += self.delA+self.getCaracter()+self.delF
			else:
				string += self.getCaracter()
			self.moveCabecote('r')
		self.cabecote = c

		print(str(string)+'    cabecote: '+str(self.cabecote))



	def escreveFita(self,caracter):
		if(self.cabecote >= 0):
			self.fita1[self.cabecote] = caracter
		else:
			self.fita2[abs(self.cabecote)] = caracter
			


	def getFita(self):
		aux = ''.join(self.fita2)
		string = aux[::-1]
		string += ''.join(self.fita1)
		return string



	def acaoEstado(self, acao):
		escrita = acao[0]
		movimento = acao[1]
		proxEstado = acao[2]
		self.escreveFita(escrita)
		self.moveCabecote(movimento)
		return proxEstado

	def acaoBloco(self, acao):
		self.pilha.append()



	def rodaPrograma2(self):
		#Escritos de boas vindas
		print('\nSimulador da Máquina de Turing ver 1.0\n')
		print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação\n')
		print('Eduardo Miranda & Thales Lima, IFMG, 2018. \n\n')

		print('Forneça a palavra inicial: ', end="")

		word = input('')
		
		# seta as variaveis que vao executar as instrucoes dos blocos
		self.fita1 = list(word)
		self.fita2 = []
		self.cabecote = 0
		self.pilha = []

		# adiciona o bloco inicial
		self.pilha.append(self.blocos[0])

		while(self.pilha):

			#print(str(self.fita1))
			blocoAtual = deepcopy(self.pilha[len(self.pilha)-1])
			#print(str(blocoAtual))

			simbAtual = self.getCaracter()
			#print(str(simbAtual))

			self.fuleragem(blocoAtual)

			acao = blocoAtual.processa(simbAtual)
			
			if(identificaAcao(acao) == 1): 
			# acao de estado
				blocoAtual.estadoAtual = self.acaoEstado(acao)
			else: 
			# acao de bloco 
				pass


			self.fuleragem(blocoAtual)

		print(self.getFita())


















	#Função que rodará o programa escrito na máquina de turing
	def rodaPrograma(self):			
		
		#Escritos de boas vindas
		print('\nSimulador da Máquina de Turing ver 1.0\n')
		print('Desenvolvido como trabalho prático para a disciplina de Teoria da Computação\n')
		print('Eduardo Miranda & Thales Lima, IFMG, 2018. \n\n')

		print('Forneça a palavra inicial: ', end="")

		word = input('')

		#coloca a palavra que o usuario digitar na primeira fita
		self.fita1 = word

		#coloca na pilha de execução o primeiro bloco
		self.pilha.append(deepcopy(self.blocos[0]))

		#enquanto houver um bloco na pilha não se sai do laço
		while(self.pilha):
			
			#Vê se a fita que deve ser lida é a da direita do 0 ou a da esquerda
			if(self.cabecote >= 0):
				simbAtual = self.fita1[self.cabecote]
			else:
				simbAtual = self.fita2[abs(cabecote)-1]
			
			#coloca-se o bloco atual em uma variavel para melhor manipulação
			blocoAtual = self.pilha[len(self.pilha)-1]

			# printa execucao
			self.fuleragem(blocoAtual)

			print(str(blocoAtual.instrucoes[blocoAtual.estadoAtual]))

			#checa se o estado em questao está dentro do bloco
			if (not blocoAtual.estadoAtual in blocoAtual.instrucoes.keys()):
				print("O estado atual não é informado neste bloco.")

			#checa se há uma transição com o simbolo atual a partir do estado atual
			if (not simbAtual in blocoAtual.instrucoes[blocoAtual.estadoAtual].keys()):
				print("Não há transições com o simbolo "+simbAtual+" do estado "+str(blocoAtual.estadoAtual))

			#acessa o ultimo bloco que está na pilha na sua listas de instrucoes com o simbolo atual do cabeçote
			restoDaInstrucao = blocoAtual.instrucoes[blocoAtual.estadoAtual][simbAtual]

			#trata-se o caso da instrução ser normal
			if(len(restoDaInstrucao) == 3):

				#coloca como estado atual o estado destino
				blocoAtual.estadoAtual = int(restoDaInstrucao[2])

				#verifica em qual fita se deve escrever e se escreve na mesma, cria-se mais tamanho caso necessário
				if(self.cabecote>=0):

					#verifica o tamanho do cabeçote e escreve na fita em seguida
					if(self.cabecote > len(self.fita1)):
						self.fita1 += (restoDaInstrucao[0])
					else:
						self.fita1 = self.fita1[:(self.cabecote-1)]+restoDaInstrucao[0]+self.fita1[(self.cabecote+1):]
						
				else:
					#verifica o tamanho do cabeçote e escreve na fita em seguida
					if(abs(self.cabecote) > len(self.fita2)):
						self.fita2 += restoDaInstrucao[0]
					else:
						self.fita2 = self.fita2[:(self.cabecote-2)]+restoDaInstrucao[0]+self.fita2[self.cabecote:]

				#move o cabeçote para a esquerda ou para a direita
				self.moveCabecote(restoDaInstrucao[1])


			#trata-se o caso da instrução ser uma do tipo que move pra um bloco
			else:
				#muda-se o estado para o estado destino
				self.blocoAtual.estadoAtual = int(restoDaInstrucao[0])

				self.pilha.append(deepcopy(blocos[self.achaId()]))