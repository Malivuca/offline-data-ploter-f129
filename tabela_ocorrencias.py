import math
import implementacoes as lib
import histogram as hs

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

	hs.plotar_tabela(intervalos, casas_decimais)

main()