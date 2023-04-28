import matplotlib as plt
import numpy as np

class Noh():
	def __init__(self, lin, col):
		self.posi= [lin, col]

		self.cima  = None
		self.baixo = None
		self.esq   = None
		self.dir   = None

		self.dist  = None
		self.pai   = None

		self.visitado = "B"
	


# anda uma unidade para cima se possível
def anda_cima(no):
	novo_no = Noh(no.posi[0], no.posi[1])
	#print(novo_no)

	if novo_no.posi[1] == 0 :#or novo_no.posi[1] == 1:# Se estiver no canto mais acima ou se for o meio(onde tem a barreira)
		return novo_no

	if novo_no.posi[1] - 1 == 1 and novo_no.posi[0] == 1:
		return novo_no
	
	else:
		
		novo_no.posi[1] = novo_no.posi[1] - 1
		return novo_no

###################################################################
def anda_baixo(no):
	novo_no = Noh(no.posi[0], no.posi[1])
	#print(novo_no)

	if novo_no.posi[1] == 2 :#or novo_no.posi[1] == 1:# Se estiver no canto mais abaixo ou se for o meio(onde tem a barreira)
		return novo_no

	if novo_no.posi[1] + 1 == 1 and novo_no.posi[0] == 1:
			return novo_no
	
	else:
		
		novo_no.posi[1] = novo_no.posi[1] + 1
		return novo_no


###################################################################
def anda_esq(no):
	novo_no = Noh(no.posi[0], no.posi[1])
	#print(novo_no)

	if novo_no.posi[0] == 0 :#or novo_no.posi[0] == 1:# Se estiver no canto mais a esquerda ou se for o meio(onde tem a barreira)
		return novo_no

	if novo_no.posi[0] - 1 == 1 and novo_no.posi[1] == 1:
			return novo_no
	
	else:

		novo_no.posi[0] = novo_no.posi[0] - 1
		return novo_no


###################################################################
def anda_dir(no):
	novo_no = Noh(no.posi[0], no.posi[1])
	#print(novo_no)

	if novo_no.posi[0] == 2 :#or novo_no.posi[0] == 1: # Se estiver no canto mais a direita ou se for o meio(onde tem a barreira)
		return novo_no
	
	if novo_no.posi[0] + 1 == 1 and novo_no.posi[1] == 1:
			return novo_no
	
	else:

		novo_no.posi[0] = novo_no.posi[0] + 1
		return novo_no
  


def expansao(no):
	no.cima  = anda_cima(no) 
	no.baixo = anda_baixo(no) 
	no.esq   = anda_esq(no)  
	no.dir   = anda_dir(no)


############################################################
############################################################
############################################################
# Busca em largura
def busca_larg(no, lin_f, col_f):
	achou = 0

	print(f"Posição inicial: {no.posi}")
	fronteira = []


	fronteira.append(no)
	no_atual = no

	i = 0
	while len(fronteira) != 0 and achou != 1:
	#while no.posi[0] != lin_f and no.posi[1] != col_f:

		no_atual = fronteira.pop(0)

		print(f"{i}: {no_atual.posi[0]}, {no_atual.posi[1]}")
		i = i + 1

		
		
		expansao(no_atual)
		#print(no_atual.cima, no_atual.baixo , no_atual.esq ,no_atual.dir)



		if no_atual.cima.visitado == "B":

			no_atual.cima.visitado == "C"
			expansao(no_atual.cima)
			fronteira.append(no_atual.cima)
		
		if no_atual.baixo.visitado == "B":

			no_atual.baixo.visitado == "C"
			expansao(no_atual.baixo)
			fronteira.append(no_atual.baixo)

		if no_atual.esq.visitado == "B":

			no_atual.esq.visitado = "C"
			expansao(no_atual.esq)
			fronteira.append(no_atual.esq)
		
		if no_atual.dir.visitado == "B":

			no_atual.dir.visitado = "C"
			expansao(no_atual.dir)
			fronteira.append(no_atual.dir)

		no_atual.visitado = "P"

		if no_atual.posi[0] == lin_f and no_atual.posi[1] == col_f:
			achou = 1


############################################################
############################################################
############################################################

def DFS(no):
	cont_lin = 1
	expansao(no)

	tempo = 0
	global n_mexe
	n_mexe = 0

	cont_dir = 0
	cont_esq = 0
	cont_cima = 0
	cont_baixo = 0
	

	# 4 primeiros caminhos (vai para cima, baixo, esq e dir)
	if no.cima.visitado  == "B":
		DFS_Visit(no.cima,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)
		
	if no.baixo.visitado  == "B":
		DFS_Visit(no.baixo,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)
		
	if no.esq.visitado == "B":
		DFS_Visit(no.esq,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)
	
	if no.dir.visitado == "B":
		DFS_Visit(no.dir,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)


def DFS_Visit(noh,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo):
	print(f"{noh.posi[0], noh.posi[1]}")

	expansao(noh)

	tempo = tempo + 1
	noh.dist = tempo
	noh.cor = "C"

	if noh.posi[0] == lin_f and noh.posi[1] == col_f:
		global n_mexe
		n_mexe = 1
		print(f"--->{noh.posi[0], noh.posi[1]}<---")
		return
	
	else:

		if noh.cima.visitado == "B":
			noh.cima.pai  = noh

			if cont_cima < 5 :
				cont_cima = cont_cima + 1
				if n_mexe == 0:
					DFS_Visit(noh.cima,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)

			else:
				cont_cima = 0
				return
		
		if noh.baixo.visitado == "B":
			noh.baixo.pai  = noh

			if cont_baixo < 5 :
				cont_baixo = cont_baixo + 1
				if n_mexe == 0:
					DFS_Visit(noh.baixo,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)

			else:
				cont_baixo = 0
				return

		if noh.esq.visitado  == "B":
			noh.esq.pai  = noh

			if cont_esq < 5 :
				cont_esq = cont_esq + 1
				if n_mexe == 0:
					DFS_Visit(noh.esq,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)

			else:
				cont_esq = 0
				return

		if noh.dir.visitado  == "B":
			noh.dir.pai  = noh

			if cont_dir < 5 :
				cont_dir = cont_dir + 1
				if n_mexe == 0:
					DFS_Visit(noh.dir,  tempo, cont_dir, cont_esq, cont_cima, cont_baixo)

			else:
				cont_dir = 0
				return
			
		
		noh.visitado = "P"
		tempo = tempo + 1



##########################################################
if __name__ == "__main__":
	print("Indique a linha e a coluna da posião final")
	# Exemplo:  0 0 ou 1 5 ou 2 2
	lin_f,col_f = input().split()

	lin_f = int(lin_f)
	col_f = int(col_f) 

	# lin_f = 2
	# col_f = 2

	
	no = Noh(0, 0)
	no.visitado = "C"

	#busca_larg(no, lin_f, col_f)

	no.visitado = "B"
	DFS(no)

	
