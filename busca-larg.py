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

	achou = 0 # flag para estado objetivo alcan

	cont_lin = 1
	while len(fila) != 0 and achou != 1: # len(fila) != 0 or
		no_atual = fila.pop(0) # Retirar o primeiro elemento da fila

		print(f"{cont_lin}: {no_atual.posiRobo, no_atual.s1, no_atual.s2}")
		cont_lin = cont_lin + 1
		
		if no_atual.dir.cor  == "B":
			no_atual.dir.cor  = "C"
			no_atual.dir.dist = no_atual.dist + 1
			no_atual.dir.pai  = no_atual
			
			expansao(no_atual.dir)
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

		if no_atual.s1 == 0 and no_atual.s2 == 0: # Condicional para decidir para onde ir
			achou = 1
#***************************************************************************************#



def DFS(no):
	cont_lin = 1
	expansao(no)

	tempo = 0
	global n_mexe
	n_mexe = 0

	cont_dir = 0
	cont_esq = 0
	cont_limp = 0

		
	if no.dir.cor  == "B":
		print("DIR")
		DFS_Visit(no.dir, cont_lin, tempo, cont_dir, cont_esq, cont_limp)
		

	if no.esq.cor  == "B":
		print("ESQ")
		DFS_Visit(no.esq, cont_lin, tempo, cont_dir, cont_esq, cont_limp)

		
	if no.limp.cor == "B":
		print("LIMP")
		DFS_Visit(no.limp, cont_lin, tempo, cont_dir, cont_esq, cont_limp)



def DFS_Visit(noh, cont_lin, tempo, cont_dir, cont_esq, cont_limp):
	print(f"{cont_lin}: {noh.posiRobo, noh.s1, noh.s2}")

	cont_lin = cont_lin + 1
	expansao(noh)

	tempo = tempo + 1
	noh.dist = tempo
	noh.cor = "C"

	if noh.s1 == 0 and noh.s2 == 0:
		global n_mexe
		n_mexe = 1
		return
	
	else:
		if noh.dir.cor  == "B":
			noh.dir.pai  = noh
			#expansao(noh.dir)

			if cont_dir < 5 and (noh.s1 != 0 or noh.s2 != 0):
				cont_dir = cont_dir + 1

				if n_mexe == 0:
					DFS_Visit(noh.dir, cont_lin, tempo, cont_dir, cont_esq, cont_limp)
			else:
				cont_dir = 0
				return

		if noh.esq.cor  == "B":
			noh.esq.pai  = noh
			#expansao(noh.esq)

			if cont_esq < 5 and (noh.s1 != 0 or noh.s2 != 0):
				cont_esq = cont_esq + 1
				
				if n_mexe == 0:
					DFS_Visit(noh.esq, cont_lin, tempo, cont_dir, cont_esq, cont_limp)
			else:
				cont_esq = 0
				return

		if noh.limp.cor == "B":
			noh.limp.pai  = noh
			#expansao(noh.limp)

			if cont_limp < 5 and (noh.s1 != 0 or noh.s2 != 0):
				cont_limp = cont_limp + 1
	
				if n_mexe == 0:
					DFS_Visit(noh.limp, cont_lin, tempo, cont_dir, cont_esq, cont_limp)
			else:
				cont_limp = 0
				return

		noh.cor = "P"
		tempo = tempo + 1


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

#robo = busca_larg(robo)

robo = DFS(robo)


# print(f"\nEstado final-> {robo.posiRobo} {robo.s1} {robo.s2}")
