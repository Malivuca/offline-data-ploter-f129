import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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

def plotar_tabela(intervalos, casas_decimais):
	data = [[intervalos[i].ocorrencias, intervalos[i].frequencia_relativa] for i in range(len(intervalos))]

	rows = ["[%f - %f)" %(round(intervalos[i].minimo, casas_decimais), round(intervalos[i].maximo, casas_decimais)) for i in range(len(intervalos))]
	columns = ["Ocorrências", "Frequêcia Relativa"]

	colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))

	fig, axs = plt.subplots()

	table = axs.table(cellText=data,
					  cellLoc="center",
					  rowLabels=rows,
					  rowLoc="center",
					  colLabels=columns,
					  colLoc="center",
					  edges="closed")
	
	axs.axis('off')
	axs.axis('tight')
	"""

	#rowColors=colors, cellColours=colors,
	

	fig, axs = plt.subplots()

	fig.patch.set_visible(False)
	axs.axis('off')
	axs.axis('tight')

	df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

	seila = axs.table(cellText=df.values, colLabels=df.columns, loc='center')	

	seila.set_fontsize(32)

	fig.tight_layout()"""

	plt.show()