import math, os

def main():
	print("Digite o numero de medicoes que deseja analisar: ", end="")

	n = int(input())

	dados = [0 for i in range(n)]
	maximo = -math.inf
	intervalos = []

	print("Entre com os dados:")

	for i in range(n):
		a = float(input())
		dados[i] = a
	    
	print("Criar os intervalos automaticamente? (Y, n): ", end ="")

	opcao = input()

	print("Quantidade de casas decimais dos intervalos: ", end="")

	casas_decimais = int(input())

	if opcao.lower() == "y":
		tamanho_intervalo = intervalo.gerar_intervalo(dados, intervalos, casas_decimais)

	elif opcao.lower() == "n":
		print("Digite os intervalos que serao analisados (min max): ")

		while maximo <= max(dados):
			minimo, maximo = map(float, input().split())
			intervalos.append(intervalo.criar_intervalo(minimo, maximo))

	else:
		print("Comando invalido. Os intervalos serao gerados automaticamente.")
		tamanho_intervalo = intervalo.gerar_intervalo(dados, intervalos, casas_decimais)

	contador(dados, intervalos)

	print("Tamanho dos intervalos\t:", round(tamanho_intervalo, casas_decimais))
	print("Valor minimo\t\t:", min(dados))
	print("Valor maximo\t\t:", max(dados))

class intervalo:
	def __init__(self, minimo, maximo, ocorrencias=0):
		self.minimo = minimo
		self.maximo = maximo
		self.ocorrencias = ocorrencias

	def criar_intervalo(minimo, maximo):
		return intervalo(minimo, maximo)

	def gerar_intervalo(dados, intervalos, casas_decimais):
		minimo = min(dados)
		maximo = max(dados)

		tamanho_intervalo = round((maximo - minimo) / math.sqrt(len(dados)), casas_decimais)

		while minimo <= maximo:
			intervalos.append(intervalo.criar_intervalo(minimo, minimo + tamanho_intervalo))
			minimo += tamanho_intervalo

		return tamanho_intervalo

def contador(dados, intervalos):
	for i in range(len(intervalos)):
		ocorrencias = 0

		for j in range(len(dados)):
			if intervalos[i].minimo <= dados[j] < intervalos[i].maximo:
				ocorrencias += 1

		frequencia_relativa = ocorrencias / (len(dados))
		
		if i == 0:
			os.system("clear")
			print("\t\t\t**TABELA DE OCORRENCIAS**")

		print("Ocorrencias no intervalo [%.4f - %.4f): %d\t| Frequencia relativa: %.2f" %(intervalos[i].minimo, intervalos[i].maximo, ocorrencias, frequencia_relativa))

main()
