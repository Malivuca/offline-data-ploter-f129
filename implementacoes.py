import math, os

# ----------------------------------------------------------------------------------------------------------
#
#
#

class intervalo:
	def __init__(self, minimo, maximo, tamanho=None, ocorrencias=0, frequencia_relativa=None):
		self.minimo = minimo
		self.maximo = maximo
		self.tamanho = tamanho
		self.ocorrencias = ocorrencias
		self.frequencia_relativa = frequencia_relativa

	# ----------------------------------------------------------------------------------------------------------
	# Funcao criar_intervalos:
	# Parametros: Todos atributos da classe intervalo.
	#
	# Inicializa uma variavel do tipo intervalo como os parametros dados.

	def criar_intervalo(minimo, maximo, tamanho=None, ocorrencias=0, frequencia_relativa=None):
		return intervalo(minimo, maximo, tamanho, ocorrencias, frequencia_relativa)

	# ----------------------------------------------------------------------------------------------------------
	# Funcao gerar_intervalos:
	# Parametros: [dados]: dados coletados no experimento.
	#             [casas_decimais]: precisao de casas decimais esperada na saida.
	#
	# Gera intervalos do tipo [minimo - maximo) e retorna um vetor com esses intervalos.

	def gerar_intervalos(dados, casas_decimais):
		intervalos = []
		minimo = min(dados)
		maximo = max(dados)

		tamanho_intervalo = round((maximo - minimo) / math.sqrt(len(dados)), casas_decimais)

		while minimo <= maximo:
			intervalos.append(intervalo.criar_intervalo(minimo, minimo + tamanho_intervalo, tamanho_intervalo))

			minimo += tamanho_intervalo

		for i in range(len(intervalos)):
			for j in range(len(dados)):
				if i != len(intervalos) - 1:
					if intervalos[i].minimo <= dados[j] < intervalos[i].maximo:
						intervalos[i].ocorrencias += 1
				else:
					if intervalos[i].minimo <= dados[j] <= intervalos[i].maximo:
						intervalos[i].ocorrencias += 1

			intervalos[i].frequencia_relativa = intervalos[i].ocorrencias / len(dados)

		return intervalos

	# ----------------------------------------------------------------------------------------------------------
	#
	#
	#

	def gerar_ocorrencias_e_frequencia_relativa(dados, intervalos):
		for i in range(len(intervalos)):
			for j in range(len(dados)):
				if i != len(intervalos) - 1:
					if intervalos[i].minimo <= dados[j] < intervalos[i].maximo:
						intervalos[i].ocorrencias += 1
				else:
					if intervalos[i].minimo <= dados[j] <= intervalos[i].maximo:
						intervalos[i].ocorrencias += 1

			intervalos[i].frequencia_relativa = intervalos[i].ocorrencias / len(dados)

# ----------------------------------------------------------------------------------------------------------
#
#
#

def tabela_ocorrencias(dados, intervalos, casas_decimais):
	for i in range(len(intervalos)):
		if i == 0:
			os.system("clear")
			print("\t\t\t**TABELA DE OCORRENCIAS**")

		if i != len(intervalos) - 1:
			print("Ocorrencias no intervalo [{} - {}): {}\t| Frequencia relativa: {:.2f}".format(round(intervalos[i].minimo, casas_decimais), round(intervalos[i].maximo, casas_decimais), intervalos[i].ocorrencias, intervalos[i].frequencia_relativa))
		
		else:
			print("Ocorrencias no intervalo [{} - {}]: {}\t| Frequencia relativa: {:.2f}".format(round(intervalos[i].minimo, casas_decimais), round(intervalos[i].maximo, casas_decimais), intervalos[i].ocorrencias, intervalos[i].frequencia_relativa))

	valor_maximo = max(dados)
	valor_medio = get_valor_medio(dados)
	desvio_padrao = get_desvio_padrao(dados, valor_medio)
	incerteza_padrao = get_incerteza_padrao(desvio_padrao, len(dados))

	if intervalos[i].tamanho:
		print("Tamanho dos intervalos\t:", round(intervalos[i].tamanho, casas_decimais))
	else:
		print("Tamanho dos intervalos\t: Variado")

	print("Valor minimo\t\t:", intervalos[0].minimo)
	print("Valor maximo\t\t:", valor_maximo)
	print("Valor medio\t\t:", round(valor_medio, casas_decimais))
	print("Desvio-padrao\t\t:", round(desvio_padrao, casas_decimais))
	print("Incerteza padrao\t:", round(incerteza_padrao, casas_decimais))

# ----------------------------------------------------------------------------------------------------------
#
#
#

def get_valor_medio(dados):
	valor_medio = 0

	for i in dados:
		valor_medio += i

	valor_medio = valor_medio / len(dados)

	return valor_medio

# ----------------------------------------------------------------------------------------------------------
#
#
#

def get_desvio_padrao(dados, valor_medio):
	desvio_padrao = 0

	for i in dados:
		desvio_padrao += (i - valor_medio) ** 2

	desvio_padrao = math.sqrt(desvio_padrao / (len(dados) - 1))

	return desvio_padrao

# ----------------------------------------------------------------------------------------------------------
#
#
#

def get_incerteza_padrao(desvio_padrao, n):
	incerteza_padrao = desvio_padrao / math.sqrt(n)

	return incerteza_padrao