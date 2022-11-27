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


def jacobi(tol, erro, k_max):
	n = len(Hilbert())            
	x = np.zeros(n)       
	x_1 = np.copy(x)       
	k = 1                 
	vec_erro = []
	
	
	while k < k_max and erro > tol: 
    		 
    		for i in range(n):
        		soma = 0
        		for j in range(n):
            			if i != j:
                			soma += (Hilbert()[i][j] * x[j]) 
                	x[i] = (vetor_b[i]-soma) / Hilbert()[i][i] 
        		

    		erro = np.linalg.norm(x-x_1) 
    		vec_erro.append(erro)         
    		x_1 = np.copy(x)              

    		
    		k += 1 
	print("iterações: ",k)
	print("O erro associado a este método é: \n", vec_erro[]) #No indice do vec erro deve ir no numero máximo de iterações
	print("O vetor solução é dado por: \n ")	
	for i in range(len(x_1)):	
		print(x_1[i])
	return vec_erro	

jacobi(10e-6, 10e5, ) # o último argumento da função deve ser o número de iterações.
