# Tabela de Ocorrencias

Script para criar uma tabela de ocorrencias para disciplina de F129 da Unicamp.

Previsão para criação de histogramas: 26/09 :)

# Como usar:

Note que este tutorial é voltado para usuários de distribuições do Linux,
portanto algumas passagens podem ser diferentes caso você use outro SO.

Prerequisitos: python3, pip, numpy, matplotlib, plotly (ver sessão de instalações)

1: Baixe os arquivos desse repositório para seu computador.

2: Vá para o diretório onde os arquivos estão (extraia os arquivos, se necessário).

3: Execute a seguinte linha em seu terminal:

python3 tabela_ocorrencias.py

4: A partir desse momento, você deve seguir os passos mostrados na tela de seu terminal.

# Observações:

Exemplos dos dados de entrada podem ser vistos na pasta "Exemplos de Entrada".

A tabela de ocorrências é gerada de acordo com as recomendações da disciplina F129 ministrada
no segundo semestre de 2019 na Unicamp.

# Instalações:

Ubuntu (Debian):

python3: sudo apt-get install python3

pip: sudo apt-get install python3-pip

numpy: pip3 install numpy

matplotlib: pip3 install matplotlib

plotly: pip3 install plotly

Fedora (no lab do IC3):

No lab do IC, python3, pip, numpy e matplotlib ja estao instalados, portanto bastar instalar o plotly:
Devemos utilizar a flag --user no final do comando pip, pois nao temos permissao de administrador.

plotly: python3 -m pip install plotly --user
