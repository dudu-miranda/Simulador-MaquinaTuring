#!/usr/bin/python
# -*- encoding:utf-8 -*-


from instrucao import identificaInstrucao


class bloco(object):
	
	"""docstring for bloco"""
	def __init__(self,idBloco,nomeBloco,estadoInical,instrucoes):
		
		super(bloco, self).__init__()
		self.instrucoes =  instrucoes # {estadoOrigem: caracter : acao(lista de comandos)}
		self.idBloco = idBloco
		self.nomeBloco = nomeBloco
		self.estadoInical = int(estadoInical)
		self.estadoAtual = self.estadoInical




	def __str__(self):
		string = 'idBloco: '+str(self.idBloco)+'   nomeBloco: '+str(self.nomeBloco)+'   estadoInical: '+str(self.estadoInical)+'\n'
		for estIni in self.instrucoes:
			string += '\testadoOrigem: '+str(estIni)+'\n'
			for caractere in self.instrucoes[estIni]:
				string += '\t\tcaracatere: '+str(caractere)+'   acao: '+str(self.instrucoes[estIni][caractere])+'\n'
			string += '\n'
		return string





	def addInstrucao(self,instrucao,tipo=5):
		if tipo == 5:
			tipo = identificaInstrucao(instrucao)

		if tipo > 2:
			n = len(instrucao)-1
			if((instrucao[n] != 'retorne') and (instrucao[len(instrucao)-1] != 'pare')):
				instrucao[n] = int(instrucao[n])

		instrucao[0] = int(instrucao[0])
		if(instrucao[0] not in self.instrucoes.keys()):
			self.instrucoes[instrucao[0]] = {}
		
		if(instrucao[1] not in self.instrucoes[instrucao[0]].keys()):
			self.instrucoes[instrucao[0]][instrucao[1]] = []

		if(tipo == 4):
			self.instrucoes[instrucao[0]][instrucao[1]] = instrucao[3:]
		else:
			self.instrucoes[instrucao[0]][instrucao[1]] = instrucao[2:]	





	def processa(self, caractere):
		#print(str(caractere))
		#print(str(self))
		if(not caractere in self.instrucoes[self.estadoAtual]):
			print('o estado ('+str(self.estadoAtual)+') nao possui o caracter ('+str(caractere)+')')
			return False

		# pega o que a instrucao manda fazer
		return self.instrucoes[self.estadoAtual][caractere]
		
