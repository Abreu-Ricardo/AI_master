# Aluno: Ricardo Abreu de Oliveira
# Descrição: 


# Os atributos s1 e s2 determinam se as salas 1 e 2 estão sujas,
# sendo 0(limpo) e 1(sujo) valores que indicam seus estados.

class No:
	def __init__(self,posiRobo, s1, s2):
		self.posiRobo = posiRobo
		self.s1   = s1
		self.s2   = s2
		self.esq  = None
		self.dir  = None
		self.limp = None


def anda_esq(n):
	noEsq = No(n.posiRobo, n.s1, n.s2)
	noEsq.posiRobo = 1
	
	return noEsq

def anda_dir(n):
	noDir = No(n.posiRobo, n.s1, n.s2)
	noDir.posiRobo = 2
	
	return noDir

def limpa(n):
	noLimpo = No(n.posiRobo, n.s1, n.s2)

	if n.posiRobo == 1:
		noLimpo.s1 = 0
	else:
		noLimpo.s2 = 0

	return noLimpo


def expansao(n):
	n.esq  = anda_esq(n)
	n.dir  = anda_dir(n)
	n.limp = limpa(n)



def caminha_arvore(n):
	while n.s1 != 0 or n.s2 != 0:
		# Primeiro cria a expansao para cada no

		# Expansao para o no atual
		expansao(n)

		# Como o objetivo é limpar a sala, escolhemos o estado onde a sala está limpa
		n = n.limp

		# Ocorre outra expansao para as outras possibilidades
		expansao(n)

		print(n.posiRobo, n.s1, n.s2)

		# Verifica qual sala ja foi limpa para pode andar para a proxima
		# Se a sala 1 estiver limpa va para a sala 2
		if n.s1 == 0:
			n = n.dir
			
		# Se a sala 2 estiver limpa va para a sala 1
		else:
			n = n.esq


	return n




# Estado inicial do robô: Posição na sala 1 e as duas salas sujas
robo = No(1, 1, 1)

print(f"Estado inicial-> {robo.posiRobo} {robo.s1} {robo.s2}\n")

robo = caminha_arvore(robo)

print(f"\nEstado final-> {robo.posiRobo} {robo.s1} {robo.s2}")
