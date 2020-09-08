#!/usr/bin/python
# -*- encoding:utf-8 -*-


from entrada import readFile, readFile2
from simulador import Simulador


fileName = 'teste.txt'
#machine = readFile(fileName)

#for inst in machine:
#	print(str(inst))


#delA = '('
#delF = ')'
#blocos = machine

#TuringMachine = MTuring(blocos, delA, delF)
#TuringMachine.rodaPrograma2()


simulador = readFile2(fileName)
print(simulador)

simulador.run()
