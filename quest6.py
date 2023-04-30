# Aluno: Ricardo Abreu de Oliveira

import math
import numpy as np
from sys import maxsize


class menor:
	def __init__(self):
		self.lin = None
		self.valor = maxsize

# Aqui fixamos a como a instancia fixada
def d(a, b):
	soma = 0


	# se alguma linha tiver um atributo faltante, ignoramos retornando o maior inteiro possivel
	# simulando um valor infinito
	if min(b) == 0:
		#print(min(b))
		return maxsize

	#print(f"{a,b}")

	# Para cada atributo realizamos a diferença e elevamos ao quadrado
	# Após todods os atributos serem somados retiramos a raíz quadrada da soma
	for i in range(1,len(a)):
		soma += (a[i] - b[i])**2

	return math.sqrt(soma)
###########################################################################

def d2(a, b ):
	soma = 0


	# se alguma linha tiver um atributo faltante, ignoramos retornando o maior inteiro possivel
	# simulando um valor infinito
	if min(b) == 0:
		#print(min(b))
		return maxsize

	#print(f"{a,b}")

	# Para cada atributo realizamos a diferença e elevamos ao quadrado
	# Após todods os atributos serem somados retiramos a raíz quadrada da soma
	for i in range(0 , len(a)):
		if i == 1:
			continue
		soma += (a[i] - b[i])**2

	return math.sqrt(soma)



###########################################################################

def d3(a, b ):
	soma = 0


	# se alguma linha tiver um atributo faltante, ignoramos retornando o maior inteiro possivel
	# simulando um valor infinito
	if min(b) == 0:
		#print(min(b))
		return maxsize

	#print(f"{a,b}")

	# Para cada atributo realizamos a diferença e elevamos ao quadrado
	# Após todods os atributos serem somados retiramos a raíz quadrada da soma
	for i in range(0 , len(a)-1):
		if i == 1:
			continue
		soma += (a[i] - b[i])**2

	return math.sqrt(soma)


###########################################################################
def calc_1(mat):
	valor = 0


	menor1 = menor()
	menor2 = menor()
	menor3 = menor()

	for i in range(0,6):
		if i != 1:
			# print(i)
			valor = d(mat[1], mat[i])
			valor = round(valor, 2)
			#print(valor)

			if valor < menor1.valor:
				menor1.valor = valor
				menor1.lin = i

			elif valor < menor2.valor:
				menor2.valor = valor
				menor2.lin = i
			
			else:#elif valor < menor3:
				menor3.valor = valor
				menor3.lin = i

	print(f"Menores distâncias:{menor1.lin, menor2.lin, menor3.lin}")
	print(f"Media KNN 2: {(mat[menor1.lin][0]+mat[menor2.lin][0])/2}\nMedia KNN 3: {(mat[menor1.lin][0] + mat[menor2.lin][0] + mat[menor3.lin][0])/3}")

###################################################################################

def calc_2(mat):
	valor = 0


	menor1 = menor()
	menor2 = menor()
	menor3 = menor()

	for i in range(0,6):
		if i != 1:
			# print(i)
			valor = d2(mat[2], mat[i])
			valor = round(valor, 2)
			#print(valor)

			if valor < menor1.valor:
				menor1.valor = valor
				menor1.lin = i

			elif valor < menor2.valor:
				menor2.valor = valor
				menor2.lin = i
			
			else:#elif valor < menor3:
				menor3.valor = valor
				menor3.lin = i

	print(f"Menores distâncias:{menor1.lin, menor2.lin, menor3.lin}")
	print(f"Media KNN 2: {(mat[menor1.lin][1]+mat[menor2.lin][1])/2}\nMedia KNN 3: {(mat[menor1.lin][1] + mat[menor2.lin][1] + mat[menor3.lin][1])/3}")



###################################################################################
def calc_3(mat):
	valor = 0


	menor1 = menor()
	menor2 = menor()
	menor3 = menor()

	for i in range(0,6):
		if i != 1:
			# print(i)
			valor = d3(mat[3], mat[i])
			valor = round(valor, 2)

			if valor < menor1.valor:
				menor1.valor = valor
				menor1.lin = i

			elif valor < menor2.valor:
				menor2.valor = valor
				menor2.lin = i
			
			else:#elif valor < menor3:
				menor3.valor = valor
				menor3.lin = i

	print(f"Menores distâncias:{menor1.lin, menor2.lin, menor3.lin}")
	print(f"Media KNN 2: {(mat[menor1.lin][2]+mat[menor2.lin][2])/2}\nMedia KNN 3: {(mat[menor1.lin][2] + mat[menor2.lin][2] + mat[menor3.lin][2])/3}")
###################################################################################

def media(mat):

	for i in range(0, 3):
		soma = 0
		for j in range(0, 6):
			#print(mat[j][i] , end=' ')
			soma += mat[j][i]
		print(f"Média aritimética da coluna {i+1}: {soma/5}")
	
###################################################################################
if __name__ == "__main__":

	#Valores escolhidos para retirar,  obj2->(O2,A1)=4   obj3->(O3,A2)=12   obj4->(O4,A3)=400 

	#m   = [[2,4,80], [4,6,160], [6,12,240], [10,20,400], [20,40,800], [30,60,1200]]
	mat = [[2,4,80], [4,6,160], [6,12,240], [10,20,400], [20,40,800], [30,60,1200]]

	mat[1][0] = 0
	mat[2][1] = 0
	mat[3][2] = 0


	
	media(mat)
	print()

	print("Distância do primeiro obj")
	calc_1(mat)
	print()
	
	print("Distância do segundo obj")
	calc_2(mat)
	print()

	print("Distância do terceiro obj")
	calc_3(mat)
	print()