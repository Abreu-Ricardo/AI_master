# Aluno: Ricardo
# Implementação da busca em largura para o exemplo
# do robô aspirador

from pprint import pprint

fila = []

def busca_larg(n):
	expansao(n)

	n.cor = "C" # cor do no passa a ser cinza
	n.dist = 0  # No raiz recebe dist 0
	fila.append(n)

	while len(fila) != 0:
		#print(fila)
		no_atual = fila.pop(0) # Retirar o primeiro elemento da fila

		print(f"{no_atual.posiRobo, no_atual.s1, no_atual.s2}")
		
		# PROBLEMA: Como andar na arvore?

		# pprint(vars(no_atual))
		# print("\n")



		if no_atual.dir.cor  == "B":
			no_atual.dir.cor  = "C"
			no_atual.dir.dist = no_atual.dist + 1
			no_atual.dir.pai  = no_atual
			
			expansao(no_atual.dir)
			#pprint(vars(no_atual.dir))
			fila.append(no_atual.dir)
			

		if no_atual.esq.cor  == "B":
			no_atual.esq.cor  = "C"
			no_atual.esq.dist = no_atual.dist + 1
			no_atual.esq.pai  = no_atual
			
			expansao(no_atual.esq)
			fila.append(no_atual.esq)
		
		if no_atual.limp.cor == "B":
			no_atual.limp.cor  = "C"
			no_atual.limp.dist = no_atual.dist + 1
			no_atual.limp.pai  = no_atual
			
			expansao(no_atual.limp)
			fila.append(no_atual.limp)
		
		no_atual.cor = "P" # Os vizinhos ja foram visitados

		#if : # Condicional para decidir para onde ir


#***************************************************************************************#
class No:
	def __init__(self,posiRobo, s1, s2):
		self.posiRobo = posiRobo
		self.s1   = s1
		self.s2   = s2

		self.esq  = None
		self.dir  = None
		self.limp = None

		self.cor  = "B"
		self.pai  = None # predecessor do vertice
		self.dist = None # distancia do vertice


#***************************************************************************************#
def anda_esq(n):
	noEsq = No(n.posiRobo, n.s1, n.s2)
	noEsq.posiRobo = 1
	
	return noEsq

#***************************************************************************************#
def anda_dir(n):
	noDir = No(n.posiRobo, n.s1, n.s2)
	noDir.posiRobo = 2
	
	return noDir

#***************************************************************************************#
def limpa(n):
	noLimpo = No(n.posiRobo, n.s1, n.s2)

	if n.posiRobo == 1:
		noLimpo.s1 = 0
	else:
		noLimpo.s2 = 0

	return noLimpo

#***************************************************************************************#
def expansao(n):
	n.esq  = anda_esq(n)
	n.dir  = anda_dir(n)
	n.limp = limpa(n)

#***************************************************************************************#



# Estado inicial do robô: Posição na sala 1 e as duas salas sujas
robo = No(1, 1, 1)

print(f"Estado inicial-> {robo.posiRobo} {robo.s1} {robo.s2}\n")

robo = busca_larg(robo)

# print(f"\nEstado final-> {robo.posiRobo} {robo.s1} {robo.s2}")
