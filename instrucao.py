#!/usr/bin/python
# -*- encoding:utf-8 -*-


def identificaInstrucao(inst):
	n = len(inst)

	if(inst[0] == 'bloco'):
		return 1 # instrucao que inicia um bloco
	elif(inst[0] == 'fim'):
		return 2 # instrucao que termina um bloco
	elif(n == 3):
		return 3 # instrucao envolvendo um bloco
	else:
		return 4 # instrucao normal


