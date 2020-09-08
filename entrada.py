#!/usr/bin/python
# -*- encoding:utf-8 -*-


from instrucao import identificaInstrucao
from bloco import bloco
from turing import Machine
from simulador import Simulador


def monta(machine, instrucao, tipo, idBloco):

	if(tipo == 1):
		# cria bloco e adiciona na lista
		b = bloco(idBloco,instrucao[1],instrucao[2], {})
		machine.append(b)
	else:
		# adiciona instrucao
		machine[idBloco].addInstrucao(instrucao, tipo)


def readFile(file):
	
	# le o arquivo identificador por 'file'
	arq = open(file, 'r+')
	contentFile = arq.readlines()
	arq.close()

	machine = list() 

	idBloco = 0

	# cria uma lista com todas as instrucoes que foram passadas no arquivo
	for line in contentFile:

		# retira comentaarios
		comentario = line.find(';')
		newLine = line[:comentario]

		# separa istrucao e retira os espacos
		instrucao = newLine.split()

		# verifica se tinha algo na linha
		if(instrucao):
			# identifica a instrucao
			tipo = identificaInstrucao(instrucao)

			# verifica se o bloco finalizou
			if(tipo==2):
				idBloco += 1
			else:
				# monta a instrucao
				monta(machine, instrucao, tipo, idBloco)
			
	return machine



def readFile2(file):
	# le o arquivo identificador por 'file'
	arq = open(file, 'r+')
	contentFile = arq.readlines()
	arq.close()

	simulator = Simulador()

	idBloco = 0

	# cria uma lista com todas as instrucoes que foram passadas no arquivo
	for line in contentFile:

		# retira comentaarios
		comentario = line.find(';')
		newLine = line[:comentario]

		# separa istrucao e retira os espacos
		instrucao = newLine.split()

		# verifica se tinha algo na linha
		if(instrucao):
			# 
			simulator.monta(instrucao)
			#print('\n\n##############################################################################')
			#print('instrucao: '+str(instrucao))
			#print(str(simulator))
			#input('')

	return simulator
			





















