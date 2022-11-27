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


def subs_retro(A, b):
	n = len(A)
	x = n * [0]

	for i in range(n-1, -1, -1):
		S = 0
		for j in range(i+1, n):
			S = S + A[i][j] * x[j]
		x[i] = (b[i] - S) / A[i][i]

	return x


def Gauss(A, b):
	n = len(A)
	for k in range(0, n-1):
		for i in range(k+1, n):
			m = -A[i][k] / A[k][k]
			for j in range(k+1, n):
				A[i][j] = m * A[k][j] + A[i][j]
			b[i] = m * b[k] + b[i]
			A[i][k] = 0

	x = subs_retro(A,b)
	return x

print(Gauss(Hilbert(), vetor_b()))


