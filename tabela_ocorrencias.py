import math

def main():
	print("Digite o numero de medicoes que deseja analisar: ", end="")

	n = int(input())
	dados = [0 for i in range(n)]
	maximo = -10000
	intervalos = [0 for i in range(math.ceil(math.sqrt(n)) + 1)]
	j = 0

	print("Entre com os dados:")

	for i in range(n):
		a = float(input())
		dados[i] = a
	    
	print("Voce deseja criar os intervalos automaticamente? (Y, n): ")

	opcao = input()

	if opcao.lower() == "y":
		intervalo.gerar_intervalo(dados, intervalos)

	elif opcao.lower() == "n":
		print("Digite os intervalos que serao analisados (min max): ")

		while maximo <= max(dados):
			minimo, maximo = map(float, input().split())
			intervalos[j] = intervalo.criar_intervalo(minimo, maximo)
			j += 1

	else:
		print("Comando invalido. Os intervalos serao gerados automaticamente.")
		intervalo.gerar_intervalo(dados, intervalos)

	contador(dados, intervalos)

class intervalo:
	def __init__(self, minimo, maximo, ocorrencias=0):
		self.minimo = minimo
		self.maximo = maximo
		self.ocorrencias = ocorrencias

	def criar_intervalo(minimo, maximo):
		return intervalo(minimo, maximo)

	def gerar_intervalo(dados, intervalos):
		tamanho_intervalo = (max(dados) - min(dados)) / math.sqrt(len(dados))
		minimo = min(dados)

		for i in range(len(intervalos)):
			intervalos[i] = intervalo.criar_intervalo(minimo, minimo + tamanho_intervalo)
			minimo += tamanho_intervalo

def contador(dados, intervalos):
	for i in range(len(intervalos)):
		ocorrencias = 0
		for j in range(len(dados)):
			if intervalos[i].minimo <= dados[j] < intervalos[i].maximo:
				ocorrencias += 1

		frequencia_relativa = ocorrencias / (len(dados))
		print("Ocorrencias do intervalo [%.4f - %.4f): %d\t|Frequencia relativa: %.2f" %(intervalos[i].minimo, intervalos[i].maximo, ocorrencias, frequencia_relativa))

main()
