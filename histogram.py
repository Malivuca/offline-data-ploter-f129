import plotly.express as px
import plotly.graph_objects as go
import plotly.io.orca as orca
import time
import os

# Função criar_intervalos:
# Cria um arquivo "histograma.png" no diretorio images/.
# Esse arquivo eh um histograma gerado automaticamente com base nos dados fornecidos.

def plotar_histograma(dados, intervalos, valor_minimo, valor_maximo, n_dados, local):
	if local.lower() == "y":
		orca.config.executable = os.path.expanduser("~") + "/.npm-packages/bin/orca"

	colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
			  '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

	colorsName = ["azul", "laranja", "verde", "vermelho", "roxo",
				  "marrom", "rosa", "cinza", "amarelo", "azul claro"]

	print_separator()

	print("Cores disponiveis:")

	for i in range(len(colors)):
		if i != len(colors) - 1:
			print("%d. %s, " %(i + 1, colorsName[i]), end="")
		else:
			print("%d. %s" %(i + 1, colorsName[i]))

	cor = int(input("Escolha a cor das barras do seu histograma: "))

	fig = go.Figure()

	fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
	fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
	
	fig.add_trace(go.Histogram(
		histfunc="count",
	    x=dados,
	    #name='Lançamentos da esfera de aço', # name used in legend and hover labels
	    marker_color=colors[cor - 1],
	    marker_line_color="black",
	    marker_line_width=1.0,
	    opacity=0.75
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
	    #title_text='Histograma de Ocorrências', # title of plot
	    #xaxis_title_text='Tempos de queda (s)', # xaxis label
	    #yaxis_title_text='Ocorrências', # yaxis label
	    xaxis=go.layout.XAxis(
        	title=go.layout.xaxis.Title(
            	text="Tempo de queda (s)",
            	font=dict(
                	family="Times New Roman",
                	size=18,
                	#color="dimgrey"
            	)
        	)
	    ),
	    yaxis=go.layout.YAxis(
	        title=go.layout.yaxis.Title(
	            text="Ocorrências",
	            font=dict(
	                family="Times New Roman",
	                size=20,
	                #color="dimgrey"
	            )
			)
	    ),
	    bargap=0.0, # gap between bars of adjacent location coordinates
		bargroupgap=0.0 # gap between bars of the same location coordinates
	)

	printProgressBar(0, 10, prefix = 'Progress:', suffix = 'Complete', length = 30)

	#fig.show()

	if not os.path.exists("images"):
		os.mkdir("images")

	for i in range(1, 1001):
		if os.path.exists("images/histograma.png"):
			if not os.path.exists("images/histograma(%d).png" % i):
				fig.write_image("images/histograma(%d).png" % i, format="png", scale=2)
				break
		else:
			fig.write_image("images/histograma.png", format="png", scale=2)
			break

		time.sleep(0.2)

		printProgressBar(i + 1, 10, prefix = 'Progress:', suffix = 'Complete', length = 30)

# ----------------------------------------------------------------------------------- -----------------------
# Função plotar_tabela:
# Cria um arquivo "tabela_de_ocorrencias.png" no diretorio images/.
# Esse arquivo eh uma tabela de ocorrencias gerada automaticamente com base nos dados fornecidos.

def plotar_tabela(intervalos, casas_decimais, valor_medio, desvio_padrao, incerteza_padrao, local):
	if local.lower() == "y":
		orca.config.executable = os.path.expanduser("~") + "/.npm-packages/bin/orca"

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

	printProgressBar(0, 10, prefix = 'Progress:', suffix = 'Complete', length = 30)

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

		time.sleep(0.2)

		printProgressBar(i + 1, 10, prefix = 'Progress:', suffix = 'Complete', length = 30)

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def print_separator():
	print("---------------------------------------------------------------")