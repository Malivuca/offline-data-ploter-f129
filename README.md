# Tabela de Ocorrencias

Script para criar uma tabela de ocorrencias para disciplina de F129 da Unicamp.

Previsão para criação de histogramas: 26/09 :)

## Como usar:

Note que este tutorial é voltado para usuários de distribuições do Linux,
portanto algumas passagens podem ser diferentes caso você use outro SO.

Pré-requisitos: `python3`, `pip`, `numpy`, `matplotlib`, `plotly` (ver sessão de instalações)

1. Baixe os arquivos desse repositório para seu computador.

2. Vá para o diretório onde os arquivos estão (extraia os arquivos, se necessário).

3. Execute a seguinte linha em seu terminal:
```bash
$ python3 tabela_ocorrencias.py
```
4. A partir desse momento, você deve seguir os passos mostrados na tela de seu terminal.

## Observações:

Exemplos dos dados de entrada podem ser vistos na pasta "Exemplos de Entrada".

A tabela de ocorrências é gerada de acordo com as recomendações da disciplina F129 ministrada
no segundo semestre de 2019 na Unicamp.

## Instalações:

### Ubuntu (Debian):

Python3: `$ sudo apt-get install python3`

pip: `$ sudo apt-get install python3-pip`

numpy: `$ pip3 install numpy`

matplotlib: `$ pip3 install matplotlib`

plotly: `$ pip3 install plotly`

### Fedora (no lab do IC3):

No lab do IC, `python3`, `pip`, `numpy` e `matplotlib` ja estao instalados, portanto bastar instalar o `plotly`
e a api `orca`.
Devemos utilizar a flag `--user` no final do comando `pip`, pois nao temos permissao de administrador.

plotly: `$ python3 -m pip install plotly --user`

Para criar a imagem com a tabela, voce precisara da api orca. Para instalar essa api, primeiramente
vamos ter que configurar o packet manager do IC. Para isso, digite os seguintes comandos em seu terminal:
```bash
$ mkdir "${HOME}/.npm-packages"
```
```bash
$ npm config set prefix "${HOME}/.npm-packages"
```
Agora abra seu o arquivo bashrc com seu editor de texto favorito e adicione as seguintes linhas:
```bash
NPM_PACKAGES="${HOME}/.npm-packages"

export PATH="$PATH:$NPM_PACKAGES/bin"

\# Preserve MANPATH if you already defined it somewhere in your config.
\# Otherwise, fall back to `manpath` so we can inherit from `/etc/manpath`.
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"
```

> Nao sabe o que eh o arquivo bashrc? Descubra o que ele eh e como acessa-lo na proxima secao!

Apos configurar o npm, use o seguinte comando para instalar a api orca:
```bash
$ npm install -g electron@1.8.4 orca
```
### Bashrc:

Para acessa-lo, digite em seu terminal:
```bash
$ "seu_editor_de_texto" ~/.bashrc
```
Se voce nao souber o que eh o arquivo bashrc e quiser ter uma nocao basica de seus usos, acesse [este link](https://www.maketecheasier.com/what-is-bashrc/) e descubra!
