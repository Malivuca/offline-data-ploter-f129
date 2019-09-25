import plotly.express as px
import plotly.graph_objects as go
import plotly
import os

# Função criar_intervalos:
# Parâmetros: Todos atributos da classe intervalo.
# Inicializa uma variável do tipo intervalo como os parametros dados.

def plotar_histograma(dados, intervalos, valor_minimo, valor_maximo, n_dados, local):
	if local.lower() == "y":
		plotly.io.orca.config.executable = os.path.expanduser("~") + "/.npm-packages/bin/orca"

	fig = go.Figure()
	fig.add_trace(go.Histogram(
	    x=dados,
	    histnorm='percent',
	    name='Lançamentos da esfera de aço', # name used in legend and hover labels
	    xbins=dict( # bins used for histogram
	        start=valor_minimo,
	        end=valor_maximo,
	        size=intervalos[0].tamanho
	    ),
	    marker_color='#EB89B5',
	    opacity=1.0
	))
	"""fig.add_trace(go.Histogram(
	    x=x1,
	    histnorm='percent',
	    name='experimental',
	    xbins=dict(
	        start=0,
	        end=2,
	        size=0.5
	    ),
	    marker_color='#330C73',
	    opacity=0.75
	))
	"""

	fig.update_layout(
	    title_text='Histograma de Ocorrências', # title of plot
	    xaxis_title_text='Intervalos', # xaxis label
	    yaxis_title_text='Ocorrências', # yaxis label
	    bargap=0.2, # gap between bars of adjacent location coordinates
	    bargroupgap=0.1 # gap between bars of the same location coordinates
	)

	#fig.show()
	if not os.path.exists("images"):
		os.mkdir("images")

	for i in range(1, 1001):
		if os.path.exists("images/histograma.png"):
			if not os.path.exists("images/histograma(%d).png" % i):
				fig.write_image("images/histograma(%d).png" % i, format="png", width=600, height=600, scale=2)
				break
		else:
			fig.write_image("images/histograma.png", format="png", width=600, height=600, scale=2)
			break

# ----------------------------------------------------------------------------------- -----------------------
# Função criar_intervalos:
# Parâmetros: Todos atributos da classe intervalo.
# Inicializa uma variável do tipo intervalo como os parametros dados.

def plotar_tabela(intervalos, casas_decimais, valor_medio, desvio_padrao, incerteza_padrao, local):
	if local.lower() == "y":
		plotly.io.orca.config.executable = os.path.expanduser("~") + "/.npm-packages/bin/orca"

	ocorrencias = [intervalos[i].ocorrencias for i in range(len(intervalos))]
	frequencia_relativa = [intervalos[i].frequencia_relativa for i in range(len(intervalos))]

	ocorrencias.append(["{}".format(round(valor_medio, casas_decimais))])
	ocorrencias.append(["{}".format(round(desvio_padrao, casas_decimais))])
	ocorrencias.append(["{}".format(round(incerteza_padrao, casas_decimais))])

	row_labels = ["[{} - {})".format(intervalos[i].minimo, intervalos[i].maximo) for i in range(len(intervalos))]

	row_labels[-1] = row_labels[-1].replace(")", "]")

	row_labels.append("Valor médio")
	row_labels.append("Desvio-padrão")
	row_labels.append("Incerteza padrão")

	column_labels = ["Intervalos", "Ocorrências", "Frequêcia Relativa"]

	# Plotting table with plotly

	header_color = "grey"
	row_even_color = "lightgrey"
	row_odd_color = "white"

	fig = go.Figure(data=[go.Table(
		columnorder=[1, 2, 3],
		columnwidth=[56, 40, 50],
		header=dict(
			values=column_labels,
			line_color="black",
			fill_color=header_color,
			align=["left", "center"],
			font=dict(color="black", size=12)
			),
		cells=dict(
			values=[row_labels, ocorrencias, frequencia_relativa],
			line_color="black",
			fill_color=[[row_even_color if i % 2 == 0 else row_odd_color for i in range(len(intervalos) + 3)] * (len(intervalos) + 3)],
			align = ["left", "center"],
			font=dict(color="black", size=14),
			height=25
			)
		)])

	#fig.show()

	if not os.path.exists("images"):
		os.mkdir("images")

	for i in range(1, 1001):
		if os.path.exists("images/tabela_de_ocorrencias.png"):
			if not os.path.exists("images/tabela_de_ocorrencias(%d).png" % i):
				fig.write_image("images/tabela_de_ocorrencias(%d).png" % i, format="png", width=600, height=600, scale=2)
				break
		else:
			fig.write_image("images/tabela_de_ocorrencias.png", format="png", width=600, height=600, scale=2)
			break

	#fig.write_image("images/fig3.jpeg", format="jpeg", width=1280, height=720, scale=3)


	"""
	Plotting with matplotlib:

	fig, axs = plt.subplots(dpi=100)

	axs.axis('off')

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

	Additional matplotlib commands:

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
	"""