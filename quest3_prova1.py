import matplotlib as plt
import numpy as np

class Noh():
	def __init__(self, lin, col):
		self.posi= [lin, col]

		self.cima  = None
		self.baixo = None
		self.esq   = None
		self.dir   = None

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




##########################################################
if __name__ == "__main__":
	print("Indique a linha e a coluna da posião final")
	# Exemplo:  0 0 ou 1 5 ou 2 2
	lin_f,col_f = input().split()

	lin_f = int(lin_f)
	col_f = int(col_f) 

	
	no = Noh(0, 0)
	no.visitado = "C"
	busca_larg(no, lin_f, col_f)
	
