import math
import numpy as np
import matplotlib.pyplot as plt
import implementacoes as lib

def main():
	n = int(input("Digite o numero de medicoes que deseja analisar: "))

	dados = [0 for i in range(n)] # Vetor para os dados

	print("Entre com os dados:")

	for i in range(n):
		dado = float(input())

		dados[i] = dado
	    
	opcao = input("Criar os intervalos automaticamente? (Y, n): ")

	casas_decimais = int(input("Quantidade de casas decimais dos intervalos: "))

	if opcao.lower() == "y":
		intervalos = lib.intervalo.gerar_intervalos(dados, casas_decimais)

	elif opcao.lower() == "n":
		maximo_dados = max(dados)
		maximo = -math.inf
		intervalos = []


		print("Digite os intervalos no formato \"min max\", sem as aspas: ")

		while maximo <= maximo_dados:
			minimo, maximo = map(float, input().split())

			intervalos.append(lib.intervalo.criar_intervalo(minimo, maximo))

		lib.intervalo.gerar_ocorrencias_e_frequencia_relativa(dados, intervalos)

	else:
		print("Comando invalido. Os intervalos serao gerados automaticamente.")

		tamanho_intervalo = intervalo.gerar_intervalo(dados, intervalos, casas_decimais)

	lib.tabela_ocorrencias(dados, intervalos, casas_decimais)

def plotar_histograma(valor_medio, desvio_padrao, ):
	"""# Fixing random state for reproducibility
	np.random.seed(19680801)

	mu, sigma = 100, 15
	x = mu + sigma * np.random.randn(10000)

	# the histogram of the data
	n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


	plt.xlabel('Smarts')
	plt.ylabel('Probability')
	plt.title('Histogram of IQ')
	plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
	plt.axis([40, 160, 0, 0.03])
	plt.grid(True)
	plt.show()"""

	n, bins, patches = plt.hist()

main()