import numpy as np
import matplotlib.pyplot as plt

def plotar_histograma(valor_medio, desvio_padrao):
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

def plotar_tabela(intervalos, casas_decimais, valor_medio, desvio_padrao, incerteza_padrao):
	data = [[intervalos[i].ocorrencias, intervalos[i].frequencia_relativa] for i in range(len(intervalos))]

	data.append(["{}".format(round(valor_medio, casas_decimais)), ""])
	data.append(["{}".format(round(desvio_padrao, casas_decimais)), ""])
	data.append(["{}".format(round(incerteza_padrao, casas_decimais)), ""])

	#plt.title(label="Tabela de Ocorrências", loc='center')

	rows = ["[{} - {})".format(intervalos[i].minimo, intervalos[i].maximo) for i in range(len(intervalos))]

	rows[-1] = rows[-1].replace(")", "]")

	rows.append("Valor médio")
	rows.append("Desvio-padrão")
	rows.append("Incerteza padrão")

	columns = ["Ocorrências", "Frequêcia Relativa"]

	fig, axs = plt.subplots(dpi=110)

	axs.axis('off')

	#axs.title(label="Tabela de Ocorrências", loc='center')
	fig.patch.set_visible(False)



	table = axs.table(cellText=data,
					  cellLoc="center",
					  rowLabels=rows,
					  rowLoc="center",
					  colLabels=columns,
					  colWidths=[0.25, 0.25],
					  loc="center")


	cellDict = table.get_celld()

	table.auto_set_font_size(False)

	table.set_fontsize(18)

	plt.show()

	"""
	for i in range(0,len(columns)):
	    cellDict[(0,i)].set_height(0.05)
	    for j in range(1,len(data)+1):
	        cellDict[(j,i)].set_height(.05)

	table.scale(1, 1)

	plt.subplots_adjust(top=1.5)
	plt.subplots_adjust(bottom=0.8)
	plt.subplots_adjust(right=0.8)
	plt.subplots_adjust(left=0.35)
	==
	axs.set_position(pos=[0.35, 0.5, 0.6, 0.6])

	colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))

	fig, axs = plt.subplots()

	fig.patch.set_visible(False)
	axs.axis('off')
	axs.axis('tight')

	Panda:

	df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

	seila = axs.table(cellText=df.values, colLabels=df.columns, loc='center')	

	seila.set_fontsize(32)

	fig.tight_layout()
	"""