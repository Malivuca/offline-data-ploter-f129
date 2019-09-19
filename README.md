# Tabela de Ocorrencias

Script para criar uma tabela de ocorrencias para disciplina de F129 da Unicamp.

Previsão para criação de histogramas: 26/09 :)

# Como usar:

Note que este tutorial é voltado para usuários de distribuições do Linux,
portanto algumas passagens podem ser diferentes caso você use outro SO.

Prerequisitos: python3, numpy (ver sessão de instalações)

1: Baixe os arquivos desse repositório para seu computador.

2: Vá para o diretório onde os arquivos estão (extraia os arquivos, se necessário).

3: Execute a seguinte linha em seu terminal:

# python3 tabela_ocorrencias.py

4: A partir desse momento, você deve seguir os passos mostrados na tela de seu terminal.

# Observações:

O formato dos dados de entrada podem ser vistos nos arquivos "dados.txt" e "intervalos.txt".

A tabela de ocorrências é gerada de acordo com as recomendações da disciplina F129 ministrada
no segundo semestre de 2019 na Unicamp.

# Instalações:

python3:

sudo apt-get install python3

numpy:

Instalação via pip:

python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

Instalação via gerenciador de arquivos:

(Ubuntu e Debian):

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

(Fedora):

sudo dnf install numpy scipy python-matplotlib ipython python-pandas sympy python-nose atlas-devel

(MAC):

sudo port install py35-numpy py35-scipy py35-matplotlib py35-ipython +notebook py35-pandas py35-sympy py35-nose
