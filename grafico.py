import numpy as np
import matplotlib.pyplot as np

def plot_erro(q, erro):
	n = np.zeros(q)

	for i in range(q):
    		n[i]=i 

	x = np.arange(0, q, 0.01)
	plt.figure(figsize=(11,5)) 
	plt.xlabel (r"Iterações") 
	plt.ylabel (r'módulo do Erro') 
	plt.title (r'Número de Iterações x Módulo do erro (n = 15)') 
	plt.plot(n, erro, color= 'red') 
	plt.grid(True) 
	plt.show() 

