import math

# Classe intervalo:
# A classe intervalo define um intervalo do tipo [minimo, maximo), (i.e., do minimo incluso, até
# o maximo nao incluso). Essa classe tem as seguintes características:
# minimo: limite inferior do intervalo.
# maximo: limite superior do intervalo.
# tamanho (opcional): tamanho do intervalo.
# ocorrencias: numero de dados que estão nos limites do intervalo.
# frequencia_relativa: o numero de ocorrencias no intervalo em relacao ao numero total de dados.

class intervalo:
	def __init__(self, minimo, maximo, tamanho=0, ocorrencias=0, frequencia_relativa=None):
		self.minimo = minimo
		self.maximo = maximo
		self.tamanho = tamanho
		self.ocorrencias = ocorrencias
		self.frequencia_relativa = frequencia_relativa
		self.name = "[%f - %f)" %(self.minimo, self.maximo)

	# ----------------------------------------------------------------------------------------------------------
	# Função criar_intervalos:
	# Parâmetros: Todos atributos da classe intervalo.
	# Inicializa uma variável do tipo intervalo como os parametros dados.

	def criar_intervalo(minimo, maximo, tamanho=0, ocorrencias=0, frequencia_relativa=None):
		return intervalo(minimo, maximo, tamanho, ocorrencias, frequencia_relativa)

	# ----------------------------------------------------------------------------------------------------------
	# Função gerar_intervalos:
	# Parâmetros: [dados]: dados coletados no experimento.
	#             [casas_decimais]: precisão de casas decimais esperada na saída.
	# Gera um vetor com variáveis do tipo intervalo com todas suas características (i.e., tamanho,
	# número de ocorrências, etc) definidas.
	# Recebe como entrada uma lista (array) com os dados analisados e o número de casas decimais esperado na precisão final dos dados.

	def gerar_intervalos(dados, casas_decimais):
		intervalos = []
		minimo = min(dados)
		maximo = max(dados)

		tamanho_intervalo = round((maximo - minimo) / math.sqrt(len(dados)), casas_decimais)

		while minimo <= maximo:
			intervalos.append(\
				intervalo.criar_intervalo(\
					round(minimo, casas_decimais),\
					round(minimo + tamanho_intervalo, casas_decimais),\
					tamanho_intervalo\
					)\
				)

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
	# Função gerar_ocorrencias_e_frequencia_relativa:
	# Gera os campos "ocorrencias" e "frequencia_relativa" de vários intervalos dispostos em uma lista (array).
	# Recebe como entrada uma lista com os dados analisados e uma lista de variáveis do tipo intervalo.

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
# Função tabela_ocorrencias:
# Gera uma tabela de ocorrências dos dados analisados. Além disso, fornece informações importantes
# a respeito dos dados, tais como: valor máximo, valor mínimo, desvio-padrão amostral e incerteza-padrão.
# Recebe como entrada uma lista (array) com os dados, uma lista de variáveis do tipo intervalo e
# o número de casas decimais esperado na precisão final dos dados.

def tabela_ocorrencias(dados, intervalos, casas_decimais):
	for i in range(len(intervalos)):
		if i == 0:
			print("\t************TABELA DE OCORRÊNCIAS************")

		if i != len(intervalos) - 1:
			print(\
				("Ocorrências no intervalo [{:." + str(casas_decimais) + "f} - {:." + str(casas_decimais) + "f}): {}" +\
					"\t| Frequência relativa: {:.2f}").format(\
					round(intervalos[i].minimo, casas_decimais),\
					round(intervalos[i].maximo, casas_decimais),\
					intervalos[i].ocorrencias,\
					intervalos[i].frequencia_relativa\
				)\
			)
		
		else:
			print(\
				("Ocorrências no intervalo [{:." + str(casas_decimais) + "f} - {:." + str(casas_decimais) + "f}]: {}" +\
					"\t| Frequência relativa: {:.2f}").format(\
					round(intervalos[i].minimo, casas_decimais),\
					round(intervalos[i].maximo, casas_decimais),\
					intervalos[i].ocorrencias,\
					intervalos[i].frequencia_relativa\
				)\
			)

	valor_maximo = max(dados)
	valor_medio = round(get_valor_medio(dados), casas_decimais)
	desvio_padrao = round(get_desvio_padrao(dados, valor_medio), casas_decimais)
	incerteza_padrao = round(get_incerteza_padrao(desvio_padrao, len(dados)), casas_decimais)

	if intervalos[0].tamanho != 0:
		print("Tamanho dos intervalos\t:", round(intervalos[i].tamanho, casas_decimais))
	else:
		print("Tamanho dos intervalos\t: Indefinido")

	print("Valor mínimo\t\t:", intervalos[0].minimo)
	print("Valor máximo\t\t:", valor_maximo)
	print(("Valor médio\t\t: {:." + str(casas_decimais) + "f}").format(valor_medio))
	print(("Desvio-padrão\t\t: {:." + str(casas_decimais) + "f}").format(desvio_padrao))
	print(("Incerteza padrão\t: {:." + str(casas_decimais) + "f}").format(incerteza_padrao))

# ----------------------------------------------------------------------------------------------------------
# Função get_valor_medio:
# Obtém o valor médio dos dados analisados.
# Recebe como entrada uma lista (array) com os dados analisados.

def get_valor_medio(dados):
	valor_medio = 0

	for i in dados:
		valor_medio += i

	valor_medio = valor_medio / len(dados)

	return valor_medio

# ----------------------------------------------------------------------------------------------------------
# Função get_desvio_padrao:
# Obtém o desvio-padrão amostral dos dados analisados.
# Recebe como entrada uma lista (array) com os dados e o valor médio desses dados.

def get_desvio_padrao(dados, valor_medio):
	desvio_padrao = 0

	for i in dados:
		desvio_padrao += (i - valor_medio) ** 2

	desvio_padrao = math.sqrt(desvio_padrao / (len(dados) - 1))

	return desvio_padrao

# ----------------------------------------------------------------------------------------------------------
# Função get_incerteza_padrao:
# Obtém a incerteza-padrão dos dados analisados.
# Recebe como entrada o desvio-padrão dos dados e o número de dados analisados.

def get_incerteza_padrao(desvio_padrao, n):
	incerteza_padrao = desvio_padrao / math.sqrt(n)

	return incerteza_padrao