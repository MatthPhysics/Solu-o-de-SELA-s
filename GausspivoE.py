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


def Trocalinha(v, i, j):
	arr = np.array(v)	
	if len(arr.shape) == 1:
		arr[i], arr[j] = arr[j], arr[i]
	else:
		arr[[i,j], :] = arr[[j,i], :] 



def GausspivotE(A, b):
	n = len(b)
	s = np.zeros(n)

	for i in range(n):
		s[i] = max(np.abs(A[i,:]))
	for k in range(0, n-1):
		p = np.argmax(np.abs(A[k:n,k])/s[k:n]) + k
		if p != k:
			Trocalinha(b, k, p)		
			Trocalinha(s, k, p)
			Trocalinha(a, k, p)
		for i in range(k+1, n):
			if A[i, k] != 0.0:
				lam = A[i, k] / A[k, k]
				A[i, k+1: n] = A[i, k+1:n] - lam*A[k, k+1:n]
				b[i] = b[i] - lam*b[k]


	b[n-1] = b[n-1] / A[n-1, n-1]
	for k in range(n-2, -1, -1):
		b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n])) / A[k, k]
	return b


print(GausspivotE(Hilbert(), vetor_b()))
