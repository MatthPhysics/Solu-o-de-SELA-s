import numpy as np

def Hilbert(n):

	M_hilbert = np.zeros((n, n))


	for linha in range(n):
		for coluna in range(n):
			M_hilbert[linha][coluna] = 1 / (((linha + 1) + (coluna + 1)) - 1)

	return M_hilbert.tolist()

def vetor_soma(m,l):
	soma = []	
	for linha in range(len(m)):
		for coluna in range(len(m)):
			if(linha == l) and (coluna >=0) : 
				soma.append(m[linha][coluna])

	return sum(soma)

def vetor_b(n): 
	vetor_b = []	
	for i in range(n):
		vetor_b.append(vetor_soma(Hilbert(n), i))
	return vetor_b

def Gausspivot(A, b):
	for i in range(len(A)):
		pivo = math.fabs(A[i][i])
		linhaPivo = i
		for j in range(i+1, len(A)):
			if math.fabs(A[j][i]) > pivo:
				pivo = math.fabs(A[j][i])
				linhaPivo = j
		
		if linhaPivo != i:
			linhaAuxiliar = A[i]
			A[i] = A[linhaPivo]
			A[linhaPivo] = linhaAuxiliar
		
			bAuxiliar = b[i]
			b[i] = b[linhaPivo]
			b[linhaPivo] = bAuxiliar
		
		for m in range(i + 1, len(A)):
			multiplicador = A[m][i]/A[i][i]
			for n in range(i, len(A)):
				A[m][n]-=multiplicador*A[i][n]
			b[m] -= multiplicador*b[i]
	
	return solucao(A, b)


def solucao(A, b):
	vetorSolucao = []
	for i in range(len(A)):
		vetorSolucao.append(0)
	linha = len(A) - 1
	while linha >= 0:
		x = b[linha]
		coluna = len(A) - 1
		while coluna > linha:
			x -= A[linha][coluna]*vetorSolucao[coluna]
			coluna -= 1
		x /= A[linha][coluna]
		linha -= 1
		vetorSolucao[coluna] = x
	print("Solução por pivotamento parcial para n = : \n")
	for j in range(len(vetorSolucao)):
		print(vetorSolucao[j])
	

Gausspivot(Hilbert(), vetor_b())

